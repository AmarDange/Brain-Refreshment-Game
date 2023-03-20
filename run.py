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
    print(colored(pyfiglet.figlet_format(message), "yellow" , attrs=["bold"]))
Welcome("Welcome  to  the  Brain  Refreshment  Game ")

def game():
    print("option [1] check_ans")
    print("option [2] Guess_Number")
    print("option [0] Exit the Brain Refershment Game.")
    print(colored("\nNote : Please enter a valid option.", "yellow",
                      attrs=["bold"]))

    
game()

option = int(input("Enter your Game Option : "))

if option == 1:
    check_ans(question, ans, attempts, score)
elif option == 2:
    guess_number()

# def option():
#     Option = input("1 for guess_number and 2 for check_ans")
#     if option == 1:
#         guess_number()
#     elif option == 2:
#         check_ans()

# option()
quiz = {
    1 : {
        "question" : "What is the first name of Iron Man?",
        "answer" : "Tony"
    },
    2 : {
        "question" : "Who is called the god of lightning in Avengers?",
        "answer" : "Thor"
    },
    3 : {
        "question" : "Who carries a shield of American flag theme in Avengers?",
        "answer" : "Captain America"
    },
    4 : {
        "question" : "Which avenger is green in color?",
        "answer" : "Hulk"
    },
    5 : {
        "question" : "Which avenger can change it's size?",
        "answer" : "AntMan"
    },
    6 : {
        "question" : "Which Avenger is red in color and has mind stone?",
        "answer" : "Vision"
    }
}

def check_ans(question, ans, attempts, score):
    """
    Takes the arguments, and confirms if the answer provided by user is correct.
    Converts all answers to lower case to make sure the quiz is not case sensitive.
    """
    if quiz[question]['answer'].lower() == ans.lower():
        print(f"Correct Answer! \nYour score is {score + 1}!")
        return True
    else:
        print(f"Wrong Answer :( \nYou have {attempts - 1} left! \nTry again...")
        return False


def print_dictionary():
    for question_id, ques_answer in quiz.items():
        for key in ques_answer:
            print(key + ':', ques_answer[key])


def intro_message():
    """
    Introduces user to the quiz and rules, and takes an input from customer to start the quiz.
    Returns true regardless of any key pressed.
    """
    print("Welcome to this fun food quiz! \nAre you ready to test your knowledge about food?")
    print("There are a total of 20 questions, you can skip a question anytime by typing 'skip'")
    input("Press any key to start the fun ;) ")
    return True



intro = intro_message()
while True:
    score = 0
    for question in quiz:
        attempts = 3
        while attempts > 0:
            print(quiz[question]['question'])
            answer = input("Enter Answer (To move to the next question, type 'skip') : ")
            if answer == "skip":
                break
            check = check_ans(question, answer, attempts, score)
            if check:
                score += 1
                break
            attempts -= 1

    break

print(f"Your final score is {score}!\n\n")
print("Want to know the correct answers? Please see them below! ;)\n")
print_dictionary()
print("Thanks for playing! 💜")

def guess_number():
    random_number = random.randint(1, 50)
    # print("Welcome ", player_name, "to the 'Number Guessing Game.' ")
    print("Welcome to the 'Number Guessing Game.' ")
    confirm_play = input("Would you like to start the game? (Enter yes/no): ")
    attempts = 0

    while confirm_play.lower() == "yes":

        guess = int(input("Guess any number between 1 to 50 : "))

        if guess < 1 or guess > 50:
            print("Please guess any number in the Range.")

        elif guess == random_number:
            # print("@@@ Congratulations ", player_name, 'You Win @@@')
            print("@@@ Congratulations You Win @@@")
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
        # print("Thanks ", player_name, "for your Time.")
        print("Thanks for your Time.")

guess_number()



# quiz = {
#     1 : {
#         "question" : "What is the first name of Iron Man?",
#         "answer" : "Tony"
#     },
#     2 : {
#         "question" : "Who is called the god of lightning in Avengers?",
#         "answer" : "Thor"
#     },
#     3 : {
#         "question" : "Who carries a shield of American flag theme in Avengers?",
#         "answer" : "Captain America"
#     },
#     4 : {
#         "question" : "Which avenger is green in color?",
#         "answer" : "Hulk"
#     },
#     5 : {
#         "question" : "Which avenger can change it's size?",
#         "answer" : "AntMan"
#     },
#     6 : {
#         "question" : "Which Avenger is red in color and has mind stone?",
#         "answer" : "Vision"
#     }
# }

# def check_ans(question, ans, attempts, score):
#     """
#     Takes the arguments, and confirms if the answer provided by user is correct.
#     Converts all answers to lower case to make sure the quiz is not case sensitive.
#     """
#     if quiz[question]['answer'].lower() == ans.lower():
#         print(f"Correct Answer! \nYour score is {score + 1}!")
#         return True
#     else:
#         print(f"Wrong Answer :( \nYou have {attempts - 1} left! \nTry again...")
#         return False


# def print_dictionary():
#     for question_id, ques_answer in quiz.items():
#         for key in ques_answer:
#             print(key + ':', ques_answer[key])


# def intro_message():
#     """
#     Introduces user to the quiz and rules, and takes an input from customer to start the quiz.
#     Returns true regardless of any key pressed.
#     """
#     print("Welcome to this fun food quiz! \nAre you ready to test your knowledge about food?")
#     print("There are a total of 20 questions, you can skip a question anytime by typing 'skip'")
#     input("Press any key to start the fun ;) ")
#     return True



# intro = intro_message()
# while True:
#     score = 0
#     for question in quiz:
#         attempts = 3
#         while attempts > 0:
#             print(quiz[question]['question'])
#             answer = input("Enter Answer (To move to the next question, type 'skip') : ")
#             if answer == "skip":
#                 break
#             check = check_ans(question, answer, attempts, score)
#             if check:
#                 score += 1
#                 break
#             attempts -= 1

#     break

# print(f"Your final score is {score}!\n\n")
# print("Want to know the correct answers? Please see them below! ;)\n")
# print_dictionary()
# print("Thanks for playing! 💜")





# def game():
#     print("option [1] Guess_Number")
#     print("option [2] Computer_Quiz")
#     print("option [0] Exit the Brain Refershment Game.")
#     print(colored("\nNote : Please enter a valid option.", "yellow",
#                       attrs=["bold"]))
    
# game()
# option = int(input("Enter your Game Option : "))
# player_name = input("Enter Your Name:  ")

# while option != 0:
#     if option == 1:
      
#         Welcome("Welcome  to  NUMBER  GUESSING  GAME ")
#         def guess_number():
#             random_number = random.randint(1, 50)
#             print("Welcome ", player_name, "to the 'Number Guessing Game.' ")
#             confirm_play = input("Would you like to start the game? (Enter yes/no): ")
#             attempts = 0

#             while confirm_play.lower() == "yes":

#                 guess = int(input("Guess any number between 1 to 50 : "))

#                 if guess < 1 or guess > 50:
#                     print("Please guess any number in the Range.")

#                 elif guess == random_number:
#                     print(colored("\n@@@ Congratulations ", player_name, 'You Win @@@', "blue", attrs=["bold"]) )
#                     # print(colored("\nCongratulations ", player_name, 'You Win", "yellow", attrs=["bold"]))
#                     attempts +=1
#                     print("It took you ", attempts, "attempts to win this Game.")
#                     break
#                 elif guess > random_number:
#                     print("Hint: Please try with smaller number.")
#                     attempts +=1

#                 elif guess < random_number:
#                     print("Hint: Please try with larger number.")
#                     attempts +=1

#             else:
#                 print("Thanks ", player_name, "for your Time.")

#         guess_number()
        
#     elif option == 2:
        
#         Welcome("Welcome  to  COMPUTER  QUIZ  GAME!! ")
#         print('NOTE: if your spelling is incorrect then it is considered as wrong answer')

#         print("Welcome ", player_name, "to the 'Computer Quiz Game.' ")

#         score = 0

#         answer = input("What does CSS stand for? ")
#         if answer == "cascading style sheets":
#             print('correct!!')
#             score += 1
#         else:
#             print('Incorrect!!!')
#             print('correct answer is --> cascading style sheets')
            
#         answer = input("What does CPU stand for? ")
#         if answer == "central processing unit":
#             print('Correct!!')
#             score += 1
#         else:
#             print('Incorrect!!!')
#             print('correct answer is --> central processing unit')

#         answer = input("What does RAM stand for? ")
#         if answer == "random access memory":
#             print('Correct!!')
#             score += 1
#         else:
#             print('Incorrect!!!')
#             print('correct answer is --> random access memory')

#         answer = input("What does HTML stand for? ")
#         if answer == "hypertext markup language":
#             print('Correct!!')
#             score += 1
#         else:
#             print('Incorrect!!!')
#             print('correct answer is --> hypertext markup language')

#         answer = input("What does PDF stand for? ")
#         if answer == "portable document format":
#             print('Correct!!')
#             score += 1
#         else:
#             print('Incorrect!!!')
#             print('correct answer is --> portable document format')

#         answer = input("What does PNG in computer image format stand for? ")
#         if answer == "portable network graphics":
#             print('Correct!!')
#             score += 1
#         else:
#             print('Incorrect!!!')
#             print('correct answer is --> portable network graphics')


#         answer = input("What does GB in computer stand for? ")
#         if answer == "gigabyte":
#             print('Correct!!')
#             score += 1
#         else:
#             print('Incorrect!!!')
#             print('correct answer is --> gigabyte')

#         answer = input("What does CD in computer stand for? ")
#         if answer == "compact disk":
#             print('Correct!!')
#             score += 1
#         else:
#             print('Incorrect!!!')
#             print('correct answer is --> compact disk')


#         answer = input("What does DVD stand for? ")
#         if answer == "digital versatile disk":
#             print('Correct!!')
#             score += 1
#         else:
#             print('Incorrect!!!')
#             print('correct answer is --> digital versatile disk')


#         answer = input("What does JSON stand for? ")
#         if answer == "javascript object notation":
#             print('Correct!!')
#             score += 1
#         else:
#             print('Incorrect!!!')
#             print('correct answer is --> javascript object notation')


#         print("You got " + str(score) + " questoins correct!")
#         print("You got " + str((score/10) *100) + "%. ")
#     else:
#         print("Invalid option")

#     print()
#     game()
#     option = int(input("Enter your Game: "))

# print("Thanks for using the programm. Goodbye")


