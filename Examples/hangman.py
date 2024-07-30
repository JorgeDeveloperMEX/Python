from random import choice

# Constantes
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
MAX_ATTEMPTS = 6

# Lista de palabras en inglés
words = ['baker', 'dinosaur', 'helipad', 'shark']

def choose_word(word_list):
    chosen_word = choice(word_list)
    unique_letters = len(set(chosen_word))
    return chosen_word, unique_letters

def get_valid_letter():
    while True:
        letter = input("Choose a letter: ").lower()
        if letter in ALPHABET and len(letter) == 1:
            return letter
        else:
            print("Invalid input. Please choose a single letter.")

def display_board(chosen_word, correct_letters):
    board = [l if l in correct_letters else '-' for l in chosen_word]
    print(' '.join(board))

def update_game_state(letter, chosen_word, correct_letters, incorrect_letters):
    if letter in chosen_word:
        correct_letters.add(letter)
        return True
    else:
        incorrect_letters.add(letter)
        return False

def print_status(incorrect_letters, attempts_left):
    print(f'Incorrect letters: {", ".join(incorrect_letters)}')
    print(f'Attempts left: {attempts_left}')

def print_win_message(chosen_word,correct_letters):
    display_board(chosen_word, correct_letters)
    print("Congratulations, you found the word!")

def print_lose_message(chosen_word):
    print(f"You ran out of attempts. The word was '{chosen_word}'.")

def play_game():
    chosen_word, unique_letter_count = choose_word(words)
    correct_letters = set()
    incorrect_letters = set()
    attempts_left = MAX_ATTEMPTS
    
    while True:
        display_board(chosen_word, correct_letters)
        print_status(incorrect_letters, attempts_left)
        
        letter = get_valid_letter()
        
        if update_game_state(letter, chosen_word, correct_letters, incorrect_letters):
            if len(correct_letters) == unique_letter_count:
                print_win_message(chosen_word,correct_letters)
                break
        else:
            attempts_left -= 1
            if attempts_left == 0:
                print_lose_message(chosen_word,correct_letters)
                break

if __name__ == "__main__":
    play_game()
