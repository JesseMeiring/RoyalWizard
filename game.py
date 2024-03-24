# TO-DO: Figure out how to manage image loading.

import sys
import time
 
import pygame
from pygame.locals import *

from Map import Map
from Camera import Camera
from roomGeneration import makeASquareRoom
 
pygame.init()
 
fps = 15
fpsClock = pygame.time.Clock()
 
width, height = 800, 640
screen = pygame.display.set_mode((width, height))

map = Map(8, 8, 1)
map.buildARoom(1,1,0,5,5)
mapSurface = pygame.Surface((width, height))
mainCamera = Camera(mapSurface, Rect(64, 64, 160, 160))

# How to time shit
# tic = time.perf_counter()
# toc = time.perf_counter()
# print(f"Downloaded the tutorial in {toc - tic:0.4f} seconds")

focus_pos: pygame.Vector2 = pygame.Vector2(3, 3)

# Game loop.
while True:
  screen.fill((0, 0, 0))
  
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    if event.type == KEYDOWN:
      if event.key == K_UP:
        focus_pos.y += 1
        # mainCamera.moveDirection("UP")
      if event.key == K_DOWN:
        focus_pos.y -= 1
        # mainCamera.moveDirection("DOWN")
      if event.key == K_LEFT:
        focus_pos.x -= 1
        # mainCamera.moveDirection("LEFT")
      if event.key == K_RIGHT:
        focus_pos.x += 1
        # mainCamera.moveDirection("RIGHT")
  
  # Update.

  # Draw.
  screen.fill('gray')
  map.drawPlane(0, mapSurface)
  mainCamera.focus(focus_pos)
  mainCamera.draw(screen)

  pygame.display.flip()
  fpsClock.tick(fps)