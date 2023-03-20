# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
import pyfiglet
from termcolor import colored

def Welcome(message):
    """
    Function to display home page
    """
    print(colored(pyfiglet.figlet_format(message), "green"))
Welcome("Welcome  to  the  Brain  Refreshment  Game ")

def game():
    print("option [1] Guess_Number")
    print("option [2] Computer_Quiz")
    print("option [0] Exit the Brain Refershment Game.")

game()
option = int(input("Enter your Game Option : "))
player_name = input("Enter Your Name:  ")

while option != 0:
    if option == 1:
      
        Welcome("Welcome  to  NUMBER  GUESSING  GAME ")
        def guess_number():
            random_number = random.randint(1, 50)
            print("Welcome ", player_name, "to the 'Number Guessing Game.' ")
            confirm_play = input("Would you like to start the game? (Enter yes/no): ")
            attempts = 0

            while confirm_play.lower() == "yes":

                guess = int(input("Guess any number between 1 to 50 : "))

                if guess < 1 or guess > 50:
                    print("Please guess any number in the Range.")

                elif guess == random_number:
                    print("@@@ Congratulations ", player_name, 'You Win @@@')
                    attempts +=1
                    print("It took you ", attempts, "attempts to win this Game.")
                    break
                elif guess > random_number:
                    print("Hint: Please try with smaller number.")
                    attempts +=1

                elif guess < random_number:
                    print("Hint: Please try with larger number.")
                    attempts +=1

            else:
                print("Thanks ", player_name, "for your Time.")

        guess_number()
        
    elif option == 2:
        
        Welcome("Welcome  to  COMPUTER  QUIZ  GAME!! ")
        print('NOTE: if your spelling is incorrect then it is considered as wrong answer')

        print("Welcome ", player_name, "to the 'Computer Quiz Game.' ")

        score = 0

        answer = input("What does CSS stand for? ")
        if answer == "cascading style sheets":
            print('correct!!')
            score += 1
        else:
            print('Incorrect!!!')
            print('correct answer is --> cascading style sheets')
            
        answer = input("What does CPU stand for? ")
        if answer == "central processing unit":
            print('Correct!!')
            score += 1
        else:
            print('Incorrect!!!')
            print('correct answer is --> central processing unit')

        answer = input("What does RAM stand for? ")
        if answer == "random access memory":
            print('Correct!!')
            score += 1
        else:
            print('Incorrect!!!')
            print('correct answer is --> random access memory')

        answer = input("What does HTML stand for? ")
        if answer == "hypertext markup language":
            print('Correct!!')
            score += 1
        else:
            print('Incorrect!!!')
            print('correct answer is --> hypertext markup language')

        answer = input("What does PDF stand for? ")
        if answer == "portable document format":
            print('Correct!!')
            score += 1
        else:
            print('Incorrect!!!')
            print('correct answer is --> portable document format')

        answer = input("What does PNG in computer image format stand for? ")
        if answer == "portable network graphics":
            print('Correct!!')
            score += 1
        else:
            print('Incorrect!!!')
            print('correct answer is --> portable network graphics')


        answer = input("What does GB in computer stand for? ")
        if answer == "gigabyte":
            print('Correct!!')
            score += 1
        else:
            print('Incorrect!!!')
            print('correct answer is --> gigabyte')

        answer = input("What does CD in computer stand for? ")
        if answer == "compact disk":
            print('Correct!!')
            score += 1
        else:
            print('Incorrect!!!')
            print('correct answer is --> compact disk')


        answer = input("What does DVD stand for? ")
        if answer == "digital versatile disk":
            print('Correct!!')
            score += 1
        else:
            print('Incorrect!!!')
            print('correct answer is --> digital versatile disk')


        answer = input("What does JSON stand for? ")
        if answer == "javascript object notation":
            print('Correct!!')
            score += 1
        else:
            print('Incorrect!!!')
            print('correct answer is --> javascript object notation')


        print("You got " + str(score) + " questoins correct!")
        print("You got " + str((score/10) *100) + "%. ")
    else:
        print("Invalid option")

    print()
    game()
    option = int(input("Enter your Game: "))

print("Thanks for using the programm. Goodbye")


