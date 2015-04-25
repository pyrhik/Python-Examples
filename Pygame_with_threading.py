#Pygame Template
#IndustrialPopsicle

import pygame
import time
import math
import random
import pyganim

#Here are some colors.
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)
blue     = (   0,   0, 255)
yellow   = ( 255, 255,   0)

pygame.init()
size = [1200,800]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game")


###########################################################################
## Variables



###############

##  Lists



###############

## Fonts

mainfont=pygame.font.Font(None,32)


###############

## Images



###############

## Animations



###############

## Functions



###############

## Classes



###############

## objects



###############
###########################################################################

done = False
mainClock = pygame.time.Clock()

# -------- Main Program Loop ----------- #

while done == False:
    ## Events


    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop

    ###############
      
    ## Logic


    
    ###############
     
    screen.fill(white)

    ##   Draw


     
    ###############
    
    pygame.display.flip()    
    mainClock.tick(20)   #FPS  

