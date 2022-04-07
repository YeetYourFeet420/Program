import os
from operator import truediv
from re import A
import pygame
pygame.init()
from time import sleep
window = pygame.display.set_mode((500,500))

should_continue = True
while should_continue == True:
    pygame.display.flip()
    troubles = pygame.event.get()
    print(troubles)
    sleep(0.1)
    for trouble in troubles:
        if trouble.type == pygame.QUIT:
            os.exit()

def Sandwich(a,b,c):
    a = "Bread"
    b = "Jelly"
    c = "Peanut Butter"
    d = "Sandwich"
    a+b+c == d
    visible_bread = False
    while visible_bread == False:
        
    

#Walk to cabinet
#Open cabinet
#No Visible Bread
#Grab Keys
#Walk to Car
#Open Car Door
#Get in Car
#Close Car Door
#Drive to store
#Walk to bread aisle
#Grab Bread
#Walk to checkout
#Pay for Bread
#Walk back to car
#Open Car Door
#Get in Car
#Close Car Door
#Return Home
#Go to Kitchen
#Place Bread Down
#Open Bread Bag
#Grab two Slices of bread
#Place the two slices on the countertop
#Go to Fridge
#Open Fridge
#Grab Jelly
#Walk back to Countertop
#Place Jelly Jar down
#Walk to Cabinet
#Open Cabinet
#Grab Peanut Butter
#Walk back to countertop
#Grab Butter Knife
#Open Jar of Peanut Butter
#Stick Knife in Jar of Peanut Butter
#Take Peanut Butter Knife and drag across first peice of Bread
#Spread the Peanut Butter out by using Knife and repeadetly drag knife across bread
#Put lid back on Jar of Peanut Butter
#Open Jar of Jelly
#Stick Knife in Jar of Jelly
#Drag Knife with Jelly across 2nd peice of bread
#Spread Jelly across the peice of Bread
#Put lid back on Jar of Jelly
#Put Jelly and Peanut Butter back where you found them
#Put both peices of bread together
#Made Sandwich
