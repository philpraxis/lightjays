#!/usr/bin/env python

import sys
#import and init pygame
import pygame
import random

pygame.init() 

#create the screen
window = pygame.display.set_mode((1000, 1000)) 

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
  couleurR = (couleurR + 1) % 256
  couleurV = (ancienposX + 2) % 256
  couleurB = (ancienposY + 3) % 256
  posSouris = pygame.mouse.get_pos()
  posX = random.randint(0,1000)
  posY = random.randint(0,1000)
  pygame.draw.rect(window, (couleurR, couleurV, couleurB), (ancienposX, ancienposY, posX, posY) )
  pygame.draw.line(window, (couleurR, couleurV, couleurB), (ancienposX, ancienposY), (posX, posY) )
  pygame.display.flip()
  ancienposX = posX
  ancienposY = posY
