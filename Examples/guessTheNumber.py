from random import randint

attempts = 0
getNumber = 0
secret_number = randint(1,100)
name = input("What's your name: ")

print(f"Hi {name}, I'm thinking in a number between 1 and 100\nYou can try 8 times and guess the number")

while attempts < 8:
    getNumber = int(input("Whats the number?: "))
    attempts += 1

    if getNumber < secret_number:
        print("My number is higher than estimated")
    elif getNumber > secret_number:
        print("MMy number is lower than estimated")
    else:
        print(f"Congratulations {name}! You have guessed in {attempts} attempts")
        break

if getNumber != secret_number:
    print(f"Sorry, attempts have been exhausted. The secret number was {secret_number}")