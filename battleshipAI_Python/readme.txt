IMPORTANT:
In order to run this program you must install Thonny IDE and download te following libraries
turtle.py, random.py, winsound.py, time.py

This proyect was developed by Jorge Alan Ramirez Elias in 2019

This project is a Naval Battle graphic videogame with AI

In this version I implement the decision tree that gives the capability of taking inteligent decisions to the computer
so that it is able to make shots with greater precision since in previous deliveries the generation of shots
it was completely random
In addition to this, I added a start window and the program  depletes the instructions as well as different sounds that are played throughout the game

Test cases:

This program does not include any function for test cases since the placement of your boats, the drawing of your shots and those of the computer
depend on the click event
therefore the way to do the test cases for this program will be by clicking on certain positions.

Tests:
Ship placement
----
Try to place ships off the board my ships
should not draw anything and print the sign that the box is invalid
Try to place several ships in the same space
I shouldn't draw anything
try to place more than 5 ships
I shouldn't draw anything
try to place boats in directions they won't fit
I shouldn't draw anything, print a sign
try to place ships that cross one another
I shouldn't draw anything, print a sign
sink all the ships
must tell you that you won
try to place a ship in a position where it does not fit in any direction for example by surrounding it with other ships

----
Shot drawing
Click outside the My shots board as it is the only place where the squares should be colored
I should not draw anything
Clicking on the position of one of the ships these are printed just after drawing both boards in the shell in row column format
The program should color the box where you clicked green
Click below row 6 since here the coordinates in y become negative
It should work correctly just like the rest of the boxes
Try to draw two shots in the same position
I should do nothing and print invalid box
Trying to fill the entire board there should be 5 boxes marked in red
----
Computer shots
The shots of the computer are generated automatically
However, if you roll in an invalid box or in which you have already drawn before, you should not tiger shots from the computer

