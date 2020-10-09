import random

random_number = random.randint(0,100)
print(random_number)

print("The Challenge:")
print("1. If a player's guess is less than 1 or greater than 100, say OUT OF BOUNDS")
print("2. On a player's first turn, if their guess is")
print("within 10 of the number, return WARM!")
print("further than 10 away from the number, return COLD!")
print("On all subsequent turns, if a guess is")
print("closer to the number than the previous guess return WARMER!")
print("farther from the number than the previous guess, return COLDER!")
print("When the player's guess equals the number, tell them they've guessed correctly and how many guesses it took!")

count = 0
guess_list = []

while True:
    guess = int(input("Take a guess: "))
    guess_list.append(guess)
    count += 1

    if guess == random_number:
        break

    if guess < 0 or guess > 100:
        print("Out of bounds!")

    if count == 0:
        if abs(guess - random_number) <= 10:
            print("WARM")
        elif abs(guess - random_number) >= 10:
            print("COLD")
    else:
        if abs(guess - random_number) < abs(guess_list[count - 1] - random_number):
            print("WARMER!")
        elif abs(guess - random_number) > abs(guess_list[count - 1] - random_number):
            print("COLDER!")

print(f"You guessed correct! in {count} attempts.")



