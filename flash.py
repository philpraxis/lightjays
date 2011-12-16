#!/usr/bin/env python

import time
import sys
#import and init pygame
import pygame
import random

from pygame.locals import *

pygame.init() 

#create the screen

# window = pygame.display.set_mode((1300, 1000)) 

modes = pygame.display.list_modes(16)
if not modes:
     print '16bit not supported'
else:
    print 'Found Resolution:', modes[0]
    pygame.display.set_mode(modes[0], FULLSCREEN, 16)
# pygame.display.set_mode(modes[0], FULLSCREEN, 16)


#pygame.draw.line(window, (255, 0, 255), (0, 0), (30, 50))
#pygame.draw.line(window, (255, 255, 255), (0, 0), (640, 480))

largeur = 400
hauteur = 400
#pygame.draw.rect(window, (0, 255, 255), (213, 260, largeur, hauteur))
#pygame.draw.circle(window, (255, 0, 255), (213, 260), 50 )

#draw it to the screen
pygame.display.flip() 

#input handling (somewhat boilerplate code):
couleurR = 0
couleurV = 0
couleurB = 0

ancienposX = 0
ancienposY = 0

# while True: 
#    for event in pygame.event.get(): 
#       if event.type == pygame.QUIT: 
#           sys.exit(0) 
#       else: 
#         couleurR = (couleurR + 1) % 256
#         couleurV = (ancienposX + 2) % 256
#         couleurB = (ancienposY + 3) % 256
#         posSouris = pygame.mouse.get_pos()
#         posX = posSouris[0]
#         posY = posSouris[1]
#         pygame.draw.rect(window, (couleurR, couleurV, couleurB), (ancienposX, ancienposY, posX, posY) )
#         pygame.draw.line(window, (couleurR, couleurV, couleurB), (ancienposX, ancienposY), (posX, posY) )
#         pygame.display.flip()
#         ancienposX = posX
#         ancienposY = posY
#         
#         print event

while True:
  couleurR = (couleurR + 100) % 256
  couleurV = (ancienposX + 33) % 256
  couleurB = (ancienposY + 66) % 256
  # posSouris = pygame.mouse.get_pos()
  posX = random.randint(0,1000)
  posY = random.randint(0,1000)
  pygame.draw.rect(window, (couleurR, couleurV, couleurB), (ancienposX, ancienposY, posX, posY) )
  pygame.draw.line(window, (couleurR, couleurV, couleurB), (ancienposX, ancienposY), (posX, posY) )
  pygame.display.flip()
  ancienposX = posX
  ancienposY = posY
  time.sleep(0.05 + random.randint(0,100) / 100.0)
  pygame.draw.rect(window, (0, 0, 0), (0, 0, 1000, 1000))
  
