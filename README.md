# Brain Refreshment Game
Brain refreshment Game is a Python terminal game which runs on Heroku.

Brain refreshment Game includes two games, first is number guessing game and second is Computer Quiz.
## Game 1: Number Guessing Game
Description: Most of the geeks from a CS (Computer Science) background, think of their very first project after doing a Programming Language a simple number guessing game. The user attempts to guess a number between 1-50, if they guess too low they are told to guess 
higher, if they guess too high they are told to guess lower, and the game continues until they guess the correct number.
## Game 2: Computer Quiz
Description: A computer quiz game in Python. The user attempts to write correct answer of quiz which are related to cpython some short cuts which we are using in day today life, if they write correct answer then at the end they will win the game. if they write some correct answer and some incoorect answer then they will have result with percentage.

[Link to the Brain Refreshment game](https://brain-refreshment-game.herokuapp.com/)

![Game shown on a range of devices](docs/am_i_responsive.PNG)

* [How to play](#How-to-play)
* [User Experience (UX)](#User-Experience-(UX))
  * [Key Information](#key-information)
  * [User Stories](#User-Stories)

* [Design](#Design)
  * [Colour Scheme](#Colour-Scheme)
  * [Graphics](#Graphics)
  
* [Features](#Features)
  * [Future features](#Future-features)

* [Technologies Used](#Technologies-Used)
  * [Languages Used](#Languages-Used)
  * [Frameworks, Libraries & Programs Used](#Frameworks,-Libraries-&-Programs-Used)

* [Testing](#Testing)
  * [Solved Bugs](#Solved-Bugs)
  * [Known Bugs](#Known-Bugs)
  * [Manual Testing](#Manual-Testing)

* [Deployment](#Deployment)
  * [Local Deployment](#Local-Deployment)
  * [Remote Deployment](#Remote-Deployment)
  * [Deploy project to Heroku](#Deploy-project-to-Heroku)
  
* [Credits](#Credits)
  * [Code](#Code)
  * [Content](#Content)
  * [Acknowledgements](#Acknowledgements)


## How to play

The object of the game is to refreshment of Brain. Hence both game are very simple and made up of purpose with mind diversion. 

#### Number Guessing Game :
If the User inputs range, let’s say from 1 to 100. And compiler randomly selected 42 as the integer. And now the guessing game started, so the user entered 50 as his/her first guess. The compiler shows “Try Again! You guessed too high”. That’s mean the random number (i.e., 42) doesn’t fall in the range from 50 to 100. That’s the importance of guessing half of the range. And again, the user guesses half of 50 (Could you tell me why?). So the half of 50 is 25. The user enters 25 as his/her second guess. This time compiler will show, “Try Again! You guessed too small”. That’s mean the integers less than 25 (from 1 to 25) are useless to be guessed. Now the range for user guessing is shorter, i.e., from 25 to 50. Intelligently! The user guessed half of this range, so that, user guessed 37 as his/her third guess.  This time again the compiler shows the output, “Try Again! You guessed too small”. For the user, the guessing range is getting smaller by each guess. Now, the guessing range for user is from 37 to 50, for which the user guessed 43 as his/her fourth guess. This time the compiler will show an output “Try Again! You guessed too high”. So, the new guessing range for users will be from 37 to 43, again for which the user guessed the half of this range, that is, 40 as his/her fifth guess.  This time the compiler shows the output, “Try Again! You guessed too small”. Leaving the guess even smaller such that from 41 to 43. And now the user guessed 41 as his/her sixth guess. Which is wrong and shows output “Try Again! You guessed too small”. And finally, the User Guessed the right number which is 42 as his/her seventh guess.

Total Number of Guesses = 7

#### Computer Quiz :
The Quiz game asks the player questions related to Computer, just general quetion. They have a chances to answer each question you don't want to take the quiz too difficult. Each correct answer will score a point. At the end of the game, the program will reveal the player's final score.

### Key information:
* User must enter a name to play
* Win or lose the user is given an option to play again
