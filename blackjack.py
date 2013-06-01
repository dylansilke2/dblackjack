 #black jack
import random
import pygame
import sys
from pygame.locals import *
ace_str = ''
house = 0

def value():
    global house
    card = random.randint(1,13) 
    global card_value
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
    house_specials = random.randint(1,4)
    name = '_'
    if (card_value == 10):
       if (house_specials == 1):
            card_sp = 'King'
            print(card_sp)
       elif (house_specials == 2):
           card_sp = 'Queen'
           print(card_sp)
       elif (house_specials == 3):
           card_sp = 'Jack'
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
def loop():
    PlayerSum = 0
    DealerSum = 0
    while PlayerSum < 21:
        strPlayerSum = ''
        RequestDeal = input("Deal: Yes/no")
        if (RequestDeal == 'yes' or RequestDeal == 'Y' or RequestDeal == 'y' or RequestDeal == 'Yes'):
            value()
            PlayerCard = card_value
            PlayerSum = PlayerSum + PlayerCard
            strPlayerSum = str(PlayerSum)
            print("Your current card total is " + strPlayerSum)
        else:
            print("You have chosen to stand. Your current card total is " + strPlayerSum)
       
        value() 
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

def graphical():
        pygame.init()
        
        DISPLAYSURF = pygame.display.set_mode((400,400))
        pygame.display.set_caption("Dylan's BlackJack")
        if (card_value == 1 and house == 1):
            image = pygame.image.load('1heart.gif')
            DISPLAYSURF.blit(image)
            pygame.display.update()
        elif (card_value == 2 and house == 1):
            image = pygame.image.load('2heart.gif')
            DISPLAYSURF.blit(image)
            pygame.display.update()
        elif (card_value == 3 and house == 1):
            image = pygame.image.load('3heart.gif')
            DISPLAYSURF.blit(image)
            pygame.display.update()
        elif (card_value == 4 and house == 1):
            image = pygame.image.load('4heart.gif')
            DISPLAYSURF.blit(image)
            pygame.display.update()
        elif (card_value == 5 and house == 1):
            image = pygame.image.load('5heart.gif')
            DISPLAYSURF.blit(image)
            pygame.display.update()
        elif (card_value == 6 and house == 1):
            image = pygame.image.load('6heart.gif')
            DISPLAYSURF.blit(image)
            pygame.display.update()
        elif (card_value == 7 and house == 1):
            image = pygame.image.load('7heart.gif')
            DISPLAYSURF.blit(image)
            pygame.display.update()
        elif (card_value == 8 and house == 1):
            image = pygame.image.load('8heart.gif')
            DISPLAYSURF.blit(image)
            pygame.display.update()
        elif (card_value == 9 and house == 1):
            image = pygame.image.load('9heart.gif')
            DISPLAYSURF.blit(image)
        elif (card_value == 10 and house == 1):
            image = pygame.image.load('10heart.gif')
            DISPLAYSURF.blit(image)
            pygame.display.update()
        elif (card_value == 1 and house == 2):
            image = pygame.image.load('1diamonds.gif')
            DISPLAYSURF.blit(image)
            pygame.display.update()
        elif (card_value == 2 and house == 2):
            image = pygame.image.load('2diamonds.gif')
            DISPLAYSURF.blit(image)
            pygame.display.update()
        elif (card_value == 3 and house == 2):
            image = pygame.image.load('3diamonds.gif')
            DISPLAYSURF.blit(image)
            pygame.display.update()
        elif (card_value == 4 and house == 2):
            image = pygame.image.load('4diamonds.gif')
            DISPLAYSURF.blit(image)
            pygame.display.update()
        elif (card_value == 5 and house == 2):
            image = pygame.image.load('5diamonds.gif')
            DISPLAYSURF.blit(image)
            pygame.display.update()
        elif (card_value == 6 and house == 2):
            image = pygame.image.load('6diamonds.gif')
            DISPLAYSURF.blit(image)
            pygame.display.update()
        elif (card_value == 7 and house == 2):
            image = pygame.image.load('7diamonds.gif')
            DISPLAYSURF.blit(image)
            pygame.display.update()
        elif (card_value == 8 and house == 2):
            image = pygame.image.load('8diamonds.gif')
            DISPLAYSURF.blit(image)
            pygame.display.update() 
        elif (card_value == 9 and house == 2):
            image = pygame.image.load('9diamonds.gif')
            DISPLAYSURF.blit(image)
            pygame.display.update()
       elif (card_value == 10 and house == 2):
            image = pygame.image.load('10diamonds.gif')
            DISPLAYSURF.blit(image)
            pygame.display.update()
        
         

