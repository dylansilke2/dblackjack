#black jack
import random
import pygame
import sys
import time
from pygame.locals import *





ace_str = ''
house = 0


"""
intro() inits the GUI and adds a very basic Welcome screen. It also keeps-alive the display.
It takes no arguements and no variables are global
This will be run first.
It needs to timeout after a few seconds and the gameboard and cards to load instead.
"""

def intro():
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((400,300))
    pygame.display.set_caption("Welcome to Blackjack")

    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 128)

    fontObj = pygame.font.Font("freesansbold.ttf", 32)
    textSurfaceObj = fontObj.render('Welcome to Blackjack', True, GREEN, BLUE)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (200, 150)
    

    while True:
            DISPLAYSURF.fill(GREEN)
            DISPLAYSURF.blit(textSurfaceObj, textRectObj,)
            
        #Main game loop
            loop()
        #Main game loop
        
            for event in pygame.event.get():
                 if event.type == QUIT:
                     pygame.quit()
                     sys.exit()

            pygame.display.update()


"""
Values decides the numerical value of the card based on a random number generation.
It supports Aces, which are decided by the player.

"""



def value():
    global house 
    global card_value
    global house_specials
    

    card = random.randint(1,13)
    card_value = 1

    if (card == 2 or card == 3 or card == 4 or card == 5 or card == 6 or card == 8 or card == 9):
        card_value = card
    elif (card == 10 or card == 11 or card == 12 or card == 13):
        card_value = 10
    else:
         ace_str = input("You have drawn an ace. Do you want it to equal 11 or 1?")
         ace = int(ace_str)
         if (ace == 1):
             card_value = 1
         elif (ace == 11):
             card_value = 11
         else: 
             error_ace_str = input("That is not a number you are allowed to chose. Please chose again")
             error_ace = int(error_ace_str)
             card_value = error_ace
    house = random.randint(1,4)
    house_specials = random.randint(1,3)
    name = '_'
    if (card_value == 10):
       if (house_specials == 1):
            card_sp = 'King'
            print(card_sp)
       elif (house_specials == 2):
           card_sp = 'Queen'
           print(card_sp)
       else:
           card_sp = 'Jack'
           print(card_sp)
      
    else:
        if (house == 1):
            str_card = str(card_value)
            print(str_card + " of hearts")
        elif house == 2:
            str_card = str(card_value)
            print(str_card + " of diamonds")
        elif house == 3:
            str_card = str(card_value)
            print(str_card + " of spades")
        else:
           str_card = str(card_value)
           print(str_card + " of clubs")


def graphical():
    
        pygame.init()
        DISPLAYSURF = pygame.display.set_mode((300,400))
        pygame.display.set_caption("BlackJack")
        POSITION = (200.0, 200.0)
        
        if (card_value == 1 and house == 1):
            image = pygame.image.load('1heart.gif')
            DISPLAYSURF.blit(image, POSITION)
            pygame.display.update()
        elif (card_value == 2 and house == 1):
            image = pygame.image.load('2heart.gif')
            DISPLAYSURF.blit(image, POSITION)
            pygame.display.update()
        elif (card_value == 3 and house == 1):
            image = pygame.image.load('3heart.gif')
            DISPLAYSURF.blit(image, POSITION)
            pygame.display.update()
        elif (card_value == 4 and house == 1):
            image = pygame.image.load('4heart.gif')
            DISPLAYSURF.blit(image, POSITION)
            pygame.display.update()
        elif (card_value == 5 and house == 1):
            image = pygame.image.load('5heart.gif')
            DISPLAYSURF.blit(image, POSITION)
            pygame.display.update()
        elif (card_value == 6 and house == 1):
            image = pygame.image.load('6heart.gif')
            DISPLAYSURF.blit(image, POSITION)
            pygame.display.update()
        elif (card_value == 7 and house == 1):
            image = pygame.image.load('7heart.gif')
            DISPLAYSURF.blit(image, POSITION)
            pygame.display.update()
        elif (card_value == 8 and house == 1):
            image = pygame.image.load('8heart.gif')
            DISPLAYSURF.blit(image, POSITION)
            pygame.display.update()
        elif (card_value == 9 and house == 1):
            image = pygame.image.load('9heart.gif')
            DISPLAYSURF.blit(image)
        elif (card_value == 10 and house == 1):
            image = pygame.image.load('10heart.gif')
            DISPLAYSURF.blit(image, POSITION)
            pygame.display.update()
        elif (card_value == 1 and house == 2):
            image = pygame.image.load('1diamonds.gif')
            DISPLAYSURF.blit(image, POSITION)
            pygame.display.update()
        elif (card_value == 2 and house == 2):
            image = pygame.image.load('2diamonds.gif')
            DISPLAYSURF.blit(image, POSITION)
            pygame.display.update()
        elif (card_value == 3 and house == 2):
            image = pygame.image.load('3diamonds.gif')
            DISPLAYSURF.blit(image, POSITION)
            pygame.display.update()
        elif (card_value == 4 and house == 2):
            image = pygame.image.load('4diamonds.gif')
            DISPLAYSURF.blit(image, POSITION)
            pygame.display.update()
        elif (card_value == 5 and house == 2):
            image = pygame.image.load('5diamonds.gif')
            DISPLAYSURF.blit(image, POSITION)
            pygame.display.update()
        elif (card_value == 6 and house == 2):
            image = pygame.image.load('6diamonds.gif')
            DISPLAYSURF.blit(image, POSITION)
            pygame.display.update()
        elif (card_value == 7 and house == 2):
            image = pygame.image.load('7diamonds.gif')
            DISPLAYSURF.blit(image, POSITION)
            pygame.display.update()
        elif (card_value == 8 and house == 2):
            image = pygame.image.load('8diamonds.gif')
            DISPLAYSURF.blit(image, POSITION)
            pygame.display.update() 
        elif (card_value == 9 and house == 2):
            image = pygame.image.load('9diamonds.gif')
            DISPLAYSURF.blit(image, POSITION)
            pygame.display.update()
        elif (card_value == 10 and house == 2):
            image = pygame.image.load('10diamonds.gif')
            DISPLAYSURF.blit(image, POSITION)
            pygame.display.update()
        elif (card_value == 1 and house == 3):
            image = pygame.image.load('1clubs.gif')
            DISPLAYSURF.blit(image, POSITION)
            pygame.display.update()
        elif (card_value == 2 and house == 3):
            image = pygame.image.load('2clubs.gif')
            DISPLAYSURF.blit(image, POSITION)
            pygame.display.update()
        elif (card_value == 3 and house == 3):
            image = pygame.image.load('3clubs.gif')
            DISPLAYSURF.blit(image, POSITION)
            pygame.display.update()
        elif (card_value == 4 and house == 3):
            image = pygame.image.load('4clubs.gif')
            DISPLAYSURF.blit(image, POSITION)
            pygame.display.update()
        elif (card_value == 5 and house == 3):
            image = pygame.image.load('5clubs.gif')
            DISPLAYSURF.blit(image, POSITION)
            pygame.display.update()
        elif (card_value == 6 and house == 3):
            image = pygame.image.load('6clubs.gif')
            DISPLAYSURF.blit(image, POSITION)
            pygame.display.update()
        elif (card_value == 7 and house == 3):
            image = pygame.image.load('7clubs.gif')
            DISPLAYSURF.blit(image, POSITION)
            pygame.display.update()
        elif (card_value == 8 and house == 3):
            image = pygame.image.load('8clubs.gif')
            DISPLAYSURF.blit(image, POSITION)
            pygame.display.update()
        elif (card_value == 9 and house == 3):
            image = pygame.image.load('9clubs.gif')
            DISPLAYSURF.blit(image, POSITION)
            pygame.display.update()
        elif (card_value == 10 and house == 3):
            image = pygame.image.load('10clubs.gif')
            DISPLAYSURF.blit(image, POSITION)
            pygame.display.update()
        elif (card_value == 1 and house == 4):
            image = pygame.image.load('1spades.gif')
            DISPLAYSURF.blit(image, POSITION)
            pygame.display.update()
        elif (card_value == 2 and house == 4):
            image = pygame.image.load('2spades.gif')
            DISPLAYSURF.blit(image, POSITION)
            pygame.display.update()
        elif (card_value == 3 and house == 4):
            image = pygame.image.load('3spades.gif')
            DISPLAYSURF.blit(image, POSITION)
            pygame.display.update()
        elif (card_value == 4 and house == 4):
            image = pygame.image.load('4spades.gif')
            DISPLAYSURF.blit(image, POSITION)
            pygame.display.update()
        elif (card_value == 5 and house == 4):
            image = pygame.image.load('5spades.gif')
            DISPLAYSURF.blit(image, POSITION)
            pygame.display.update()
        elif (card_value == 6 and house == 4):
            image = pygame.image.load('6spades.gif')
            DISPLAYSURF.blit(image, POSITION)
            pygame.display.update()
        elif (card_value == 7 and house == 4):
            image = pygame.image.load('7spades.gif')
            DISPLAYSURF.blit(image, POSITION)
            pygame.display.update()
        elif (card_value == 8 and house == 4):
            image = pygame.image.load('8spades.gif')
            DISPLAYSURF.blit(image, POSITION)
            pygame.display.update()
        elif (card_value == 9 and house == 4):
            image = pygame.image.load('9spades.gif')
            DISPLAYSURF.blit(image, POSITION)
            pygame.display.update()
        elif (card_value == 10 and house == 4):
            image = pygame.image.load('1spades.gif')
            DISPLAYSURF.blit(image, POSITION)
            pygame.display.update()



"""
Loop is the main game loop, it takes in values generated by value()
and it also activates the graphical() and intro()
It evaluates the winning conditions.

TODO:
Needs to be properly integrated with pygame, as quitting is currently problematic.

Change all the CLI outputs to GUI outputs with pygame.
"""
def loop():
    PlayerSum = 0
    DealerSum = 0
    while PlayerSum < 21:
        strPlayerSum = ''
        RequestDeal = input("Deal: Yes/no")
        if (RequestDeal == 'yes' or RequestDeal == 'Y' or RequestDeal == 'y' or RequestDeal == 'Yes'):
            value()
            graphical()
            PlayerCard = card_value
            PlayerSum = PlayerSum + PlayerCard
            strPlayerSum = str(PlayerSum)
            print("Your current card total is " + strPlayerSum)
        else:
            print("You have chosen to stand. Your current card total is " + strPlayerSum)
       
        value()
        graphical()
        print("The dealer is now being dealt cards")
        DealerCard = card_value 
        DealerSum = DealerSum + DealerCard
        strDealer = str(DealerSum)
        DealerValue = DealerSum
        print("The dealers card total is " + strDealer)
        if DealerSum > 21:
                print("The dealer has gone over. You win.")
        else: continue
        
    if (PlayerSum == 21):
        print("You have hit 21!!!!!")
    else:
        play_again = 'Yes'
        play_again = input("You went over. Do you want to play again? Yes/no")
    if (play_again == 'Yes' or play_again == 'y' or play_again == "yes" or play_again == 'Yes'):
        loop()
    else:
        print("Thanks for playing. Send all your money to dylansilke@gmail.com")
#------------------Main game loop------------------------
#loop()

#-------------------Main game loop-----------------------


            
        
         

