from pathlib import Path,PurePath
import os
import sys

# Ruta base para las recetas
mi_ruta =  Path(__file__).parent.resolve() / "Recetas"
if not mi_ruta.is_dir():
    mi_ruta.mkdir()

def contar_recetas(ruta):
    """Cuenta el número de archivos .txt en la ruta dada."""
    return len(list(ruta.glob("**/*.txt")))

def limpiar_pantalla():
    """Limpia la pantalla de la terminal según el sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    """Muestra el menú principal y devuelve la opción seleccionada."""
    opciones = [
        "[1] - Leer receta",
        "[2] - Crear receta nueva",
        "[3] - Crear categoría nueva",
        "[4] - Eliminar receta",
        "[5] - Eliminar categoría",
        "[6] - Salir del programa"
    ]
    
    print('*' * 50)
    print('*' * 5 + " Bienvenido al administrador de recetas " + '*' * 5)
    print('*' * 50)
    print(f"\nLas recetas se encuentran en {mi_ruta}")
    print(f"Total recetas: {contar_recetas(mi_ruta)}\n")
    
    print("\nElige una opción:")
    for opcion in opciones:
        print(opcion)
    
    while True:
        eleccion_menu = input()
        if eleccion_menu.isdigit() and 1 <= int(eleccion_menu) <= 6:
            return int(eleccion_menu)

def mostrar_categorias(ruta):
    """Muestra las categorías (carpetas) y devuelve una lista con ellas."""
    print("Categorías:")
    lista_categorias = []
    if Path(ruta).is_dir():
        lista_categorias = [carpeta for carpeta in ruta.iterdir()if carpeta.is_dir() ]
        for idx, categoria in enumerate(lista_categorias, start=1):
            print(f"[{idx}] - {categoria.name}")
    return lista_categorias

def elegir_opcion(lista, mensaje):
    """Permite al usuario elegir una opción de una lista y devuelve el ítem seleccionado."""
    while True:
        eleccion = input(mensaje)
        if eleccion.isdigit() and 1 <= int(eleccion) <= len(lista):
            return lista[int(eleccion) - 1]

def mostrar_recetas(ruta):
    """Muestra las recetas (archivos .txt) y devuelve una lista con ellas."""
    print("Recetas:")
    lista_recetas = [receta for receta in ruta.glob('*.txt')]
    for idx, receta in enumerate(lista_recetas, start=1):
        print(f"[{idx}] - {receta.name}")
    return lista_recetas

def leer_receta(receta):
    """Lee y muestra el contenido de una receta."""
    print(receta.read_text())

def crear_receta(ruta):
    """Crea una nueva receta en la ruta dada."""
    while True:
        nombre_receta = input("Escribe el nombre de tu receta (sin extensión): ") + '.txt'
        ruta_nueva = ruta / nombre_receta
        if not ruta_nueva.exists():
            contenido_receta = input("Escribe tu nueva receta: ")
            ruta_nueva.write_text(contenido_receta)
            print(f"Tu receta {nombre_receta} ha sido creada")
            break
        else:
            print("Lo siento, esa receta ya existe.")

def crear_categoria(ruta):
    """Crea una nueva categoría en la ruta dada."""
    while True:
        nombre_categoria = input("Escribe el nombre de la nueva categoría: ")
        ruta_nueva = ruta / nombre_categoria
        if not ruta_nueva.exists():
            ruta_nueva.mkdir()
            print(f"Tu nueva categoría {nombre_categoria} ha sido creada")
            break
        else:
            print("Lo siento, esa categoría ya existe.")

def eliminar_receta(receta):
    """Elimina una receta específica."""
    receta.unlink()
    print(f"La receta {receta.name} ha sido eliminada")

def eliminar_categoria(categoria):
    """Elimina una categoría específica."""
    categoria.rmdir()
    print(f"La categoría {categoria.name} ha sido eliminada")

def volver_inicio():
    """Permite al usuario volver al menú principal."""
    while input("\nPresione V para volver al menú: ").strip().lower() != 'v':
        pass

def main():
    """Función principal del programa."""
    finalizar_programa = False
   
    while not finalizar_programa:
        limpiar_pantalla()
        print(mi_ruta)
        menu_opcion = mostrar_menu()

        match( menu_opcion) :
            case 1:
                categorias = mostrar_categorias(mi_ruta)
                if bool(categorias):
                    categoria = elegir_opcion(categorias, "\nElige una categoría: ")
                    recetas = mostrar_recetas(categoria)
                    receta = elegir_opcion(recetas, "\nElige una receta: ")
                    leer_receta(receta)
                else:
                    print("\nNo existen Categorias, creear una nueva.")
                
                volver_inicio()
            case 2:
                categorias = mostrar_categorias(mi_ruta)
                if bool(categorias):
                    categoria = elegir_opcion(categorias, "\nElige una categoría: ")
                    crear_receta(categoria)
                volver_inicio()
            case 3:
                crear_categoria(mi_ruta)
                volver_inicio()
            case 4:
                categorias = mostrar_categorias(mi_ruta)
                categoria = elegir_opcion(categorias, "\nElige una categoría: ")
                recetas = mostrar_recetas(categoria)
                receta = elegir_opcion(recetas, "\nElige una receta: ")
                eliminar_receta(receta)
                volver_inicio()
            case 5:
                categorias = mostrar_categorias(mi_ruta)
                categoria = elegir_opcion(categorias, "\nElige una categoría: ")
                eliminar_categoria(categoria)
                volver_inicio()
            case 6:
                finalizar_programa = True
                print("Programa terminado.")
       

if __name__ == "__main__":
    main()
