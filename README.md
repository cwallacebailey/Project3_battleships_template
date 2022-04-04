# Battleships

## Overview 
---
This project is a computerised game of battleships housed in a mock terminal on Heroku. The project has been an opportunity to gain knowledge and experience in an object orientated language, here python, and use classes, methods and nested 'if' statements along with ASCII artwork to create an enjoyable bug free playable game where a user faces the computer with two difficulty settings

To see the finished product please follow the link below by clicking Ctrl + the link to open in a new tab: 

![Battle Ships](readme_images/battle_ships.gif)

[Link to Heroku - Battle Ships](https://dashboard.heroku.com/apps/project3battleships)



## Table of Contents

## Design
---

### User Story:
---

### User needs 
Users will want to: 
* Understand what the game is from opening the app
* Have access to game instructions / rules from the opening screen
* Have a storyline to follow, more than just a simple game of battleships
* Be able to play the game without any bugs in a clear way
* Have access to a variety of difficulty settings 

### Aims
As a result of the above the aims are straight forward
* Make the purpose of the game clear from the offset
* Create a rules page that can be accessed by the user
* Produce a storyline for the user to follow with imagery
* Ensure no bugs are present in the game and it works as intended
* Create a Hard and Easy mode to play through 

### Plan of Attack

In order to achieve the above aims the app will: 
* Provide a welcome screen with ASCII artwork to make it clear what the game is
* The welcome screen will provide access to the game rules
* Use ASCII Art to create an engaging intro
* Ensure user inputs are usable by the code and that no bugs are present through testing
* Create more than one difficulty setting by allowing the ocmputer to guess more intelligently 

## Features

### General Features
---
In order to give the intro sequences a more smooth feel I employed a "slow type" function used throughout many of the other Python scripts. In places this replaced the print function to make the user feel more like they were watching an event unfold or part of a conversation. 

![Slow Type](readme_images/slow_type_animation.gif)

[return to contents](<#contents>)

### Welcome Screen
---
The welcome screen gives the user three options: 

1. Using 'P' the user is navigated through the full intro sequence before the main game
2. Using 'R' the user is navigated to the rules page
3. Using 'S' the user is navigated to the game skipping most of the intro sequence up to the username entry section

![Welcome Screen](readme_images/welcome_screen.png)

The code behind this allows the user to type either lower or uppercase letters to continue. If nothing or a letter which is not 'P', 'R' or 'S' is typed the screen refreshes and says "Let's try that again"

![Welcome Screen error](readme_images/welcome_error.png)

[return to contents](<#contents>)

### Intro Sequence
---
In order to create a story line to add intrigue to the game I employed ASCII artwork along with the slow type effect noted above to help the user feel engaged with the app. This sequence is accessed if the user selects the "Ready to play" option from the welcome screen by typing 'P'

![Ship Animation](readme_images/intro_sequence.gif)

The user is given the option to return to the main menu from this point. The user can use upper or lowercase letters to coninue or to return to the main menu (this could be to double check the rules before playing)

![Continue](readme_images/continue.png)

If the user enters something other than 'y' or 'n' the screen refreshes and they see the below

![Continue](readme_images/continue_error.png)

[return to contents](<#contents>)

### Rules
---
Accessed by typing 'R' the rules are two pages which add to the backstory of the game and explain what the user needs to know to play. They also justify why you can't see the enemy ships and why the ships are placed randomly throughout the board. The user is told to 'hit enter to continue', in reality any key can be pressed. 

Page 1: 

![rules pg 1](readme_images/rules.png)

Page 2: 

![rules pg 2](readme_images/rules2.png)

[return to contents](<#contents>)

### Username Entry including error handling
---

Whether the user selects 'P' or 'S' at the welcome screen they are either taken indirectly (via 'P') or directly (via 'S') to the username entry screen. To help the user feel engaged the app asks for their name. 

![Username Entry](readme_images/username_entry.png)

The user can enter anything they like here except for spaces or no username. This is done by stripping the input of all spaces and counting the length of the name left behind. If length of the input less spaces is zero they will see the screen below: 

![Username check](readme_images/username_check.png)

Once a working username is entered the user is welcomed onboard the ship and a short sequence is played saying "Lets Hunt Pirates... BATTLE SHIPS" (see the [intro sequence](<#intro-sequence>) or below to watch a truncated version: 

![Username check](readme_images/lets_hunt_animation.gif)

[return to contents](<#contents>)

### Easy or Hard Mode
---

The game has two modes, an easy mode or a hard mode and the user is invited to select which they would like in a text where easy and hard are capitalised to make it obvious what the text is asking the user to choose. 

![Easy or Hard](readme_images/easy_or_hard.png)

As with all selections so far upper or lower case can be used. If the user types something other than a 'y' or 'n' then they are invited to try again. The second time the text is printed to the terminal a "Print" is used instead of typing slowly as this is a big piece of text and watching it type out again could be frustrating: 

![Easy or Hard](readme_images/easy_hard_check.png)

If the user selects 'Y' hardmode is activated (becomes True in the code) and the next text reads "Very Nice, we will be world famous". If easy is selected the text reads "Why risk it, lets get our first mate". 

The difference between the two modes is essentially: 

Easy - Each turn the computer guesses a random location regardless of whether or not it hit a target in the previous round. 

Hard - The computer guesses at random until it hits a target. Once it hits a target it iterates around the hit by one space to see if other targets are there. These are added to an array and the computer targets these coordinates in the next rounds until the array length is zero afterwhich the computer returns to guessing at random. 

In order to develop the hard mode I create a simulation in which the computer tried to clear the board as quick as it could without any user input. In Easy mode for a 5x5 board this took between 23 and 25 turns. With the hardmode iteration this bacame around 12 turns. When testing the game I beat the easy mode everytime. I beat hardmode around one in ten tries. 

[return to contents](<#contents>)

### Gameplay

Initially the user is presented with the view below showing their ship placement and a blank board for the computer: 

![Board](readme_images/board.png)

The user always goes first and must enter a row, then a column. If either the row or column chosen is not between 1 and 8 they are asked to choose again. 

![valid row](readme_images/valid_row.png)

Once the user has chosen their first coordinate if they miss i.e. a ship is not at the coordinate they chose the text "Miss!" appears. They are then warned that the computer is taking their turn and "getting ready to shoot!!"

![miss](readme_images/miss.png)

The user is then told if the computer was successful in hitting any of their ships and the board is re-printed to the terminal, updated for location shot at: 

![First Turn](readme_images/first_turn.png)

If a miss is made then the screen is updated with an "M" in a circle to make it clearer. If a hit is made then a skull and crossbone appears over the hit. If the user makes a hit the text reads "direct hit, well done". If the computer makes a hit the text reads "One of our ships has been hit!": Note the skull and crossbone can be seen in the bottom of the screen shot below, coordinate 8, 1 

![Computer hit](readme_images/computer_hit.png)

If the user chooses coordinates they have already show at they are shown the warning below and asked to choose again: 

![Shot before](readme_images/shot_before.png)

Once a specific ship has been destroyed, be it the users or the computers that ship is named (this is outlined in the rules)

![Ship Gone](readme_images/ship_gone.png)

The game continues until either the user or the computer have no ships left. If the user wins they are shown a "You Win" animation before being taken back to the welcome screen. If the user loses (shown in the animation below) they are shown a "You Lose" animation: 

![Ship Gone](readme_images/game_over_animation.gif)

## Future Enhancements