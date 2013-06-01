dblackjack
==========

A basic implementation of blackjack -- with a GUI

If you want to contribute to the project, there are a couple of pre-requisites:
it is written in Python3.3, so you need to have downloaded this version.
It uses the Pygame library, which can be downloaded here http://www.pygame.org/download.shtml
Close python when you are installing this.
Get the one named pygame-1.9.2a0.win32-py3.2.msi if you have a Windoze computer.
To test python open the python prompt and type 'import pygame'. If this works, the install suceeded.



For Windows, download  Github for Windows, make an account and configure it.
When you are in, search for 'dblackjack under the Github tab and then clone 'dblackjack'
Then right-click the repository in your local tab and click  'open in explorer'.
Make a short-cut of this folder and drag it to your desktop.
This is now your repo and all the changes you make there can be commited to the server.
Once you have made changes and tested them drag them to your shortcut.
Open Github and on the right of the window there should be a error message 'Not Commited'
Follow the prompts to commit your changes to the server.



Commit early and commit often.
There should be very little that is not in a function.
Use the standard indentation that IDLE has.

Function calls with parameters should look like thi: foo(hello,world) or foo(hello) NOT bar( hello, world ) or bar ( hello )


Print statements should be print('whatever') NOT print ('whatever')


TODO:
Special cards such as the Queen, Jack, King and Ace currently don't work with the graphical function because the graphical function uses the card_value variable which assigns all such cards to '10'

Solution:
Create another global variable that tracks these special cards.


Betting needs to be introduced.



GUI needs some work and a gameboard.
