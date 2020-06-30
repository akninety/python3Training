from random import randint

num = randint(0,100)
numList = []
count = 0

print("Pick a number from 1-100")
print("If your first guess is within +/- 10 numbers the game will display 'WARM!'.  If it is further than +/- 10 numbers the game will print 'COLD!'")
print("After the first attempt, subsequent guesses will print colders/warmer based on the previous guess.")
print("When the player guesses the random number.  The game will display the amount of tries it took as well as the number.")

while True:
    print("Take a guess: ")
    guess = int(input())
    numList.append(guess)

    if guess == num:
        print(f"You guessed right! It took you {len(numList)} attempts.")
        break
    
    if guess < 0:
        print("OUT OF BOUNDS!")
    elif guess > 100:
        print("OUT OF BOUNDS!")

    if count == 0:
        if abs(guess-num) <= 10:
            print("WARM!")
        else:
            print("COLD!")
    else:
        if abs(num-guess) < abs(num-numList[-2]):
            print("WARMER")
        else:
            print("COLDER")

    count += 1