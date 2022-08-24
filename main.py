from ast import While
import imp
from multiprocessing import Event
import pygame
from configs.config_main import *
from colors import *

pygame.init()
surface = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# temp
player_position = (HALF_WIDTH, HALF_HEIGHT)
player_angle = 0
player_speed = 2

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()

	surface.fill(BLACK)
	
	pygame.draw.circle(surface, GREEN, player_position, 12)

	pygame.display.flip() # update display image
	clock.tick()