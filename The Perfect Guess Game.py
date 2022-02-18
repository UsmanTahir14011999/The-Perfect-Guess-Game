import random
from playsound import playsound
randNumber = random.randint(1, 100)
# print(randNumber)
userGuess = None
guesses = 0
playsound("D:\\Usman\\PYTHON\PROJECTS\\The Perfect Guess Game\\house.mp3")
while(userGuess != randNumber):
    userGuess = int(input("Enter your guess: "))
    guesses += 1
    if(userGuess==randNumber):
        print("You guessed it right!")
        playsound('D:\\Usman\\PYTHON\PROJECTS\\The Perfect Guess Game\\win.mp3')
    else:
        if(userGuess>randNumber):
            print("You guessed it wrong! Enter a smaller number/guess")
        else:
            print("You guessed it wrong! Enter a larger number/guess")

print(f"You Guessed the Number in {guesses} guesses")
with open("hiscore.txt","r") as f:
    hiscore = int(f.read())
if(guesses<hiscore):
    print("You Have Just Broken the High Score!")
    with open("hiscore.txt","w") as f:
        f.write(str(guesses))
else:
    playsound('D:\\Usman\\PYTHON\PROJECTS\\The Perfect Guess Game\\lose.mp3')
    print(f"You Failed to Broke the High Score!.\n The High Score is {hiscore}.\n TRY AGAIN")