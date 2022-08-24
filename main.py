import pygame
from configs.config_main import *
from colors import *
from player import Player
import math

pygame.init()
surface = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

player = Player()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()

	player.update_movement()

	surface.fill(BLACK)
	
	pygame.draw.circle(surface, GREEN, player.position, 12)

	pygame.display.flip() # update display image
	clock.tick(TARGET_FPS)