import random

number = random.randint(1,10) # the number to be guessed will fall between 1 and 10.
player = input('Please Enter your name: ')
guessNum = 0
print("Alright! " + player + " Guess a number from 1 to 10.\nYou have total 5 chances.")

while guessNum < 5:
    guess = int(input())
    guessNum += 1
    
    if guess > number:
        print(f'the number is smaller than {guess}. Try again')
    if guess < number:
        print(f'the number is larger than {guess}. Try again')
    if guess == number:
        break

if guess == number:
     print(f"Yay! the correct number was {number}. You won!!")
else:
    print(f"You've lost all 5 chances. The number was {number}.")
