import pygame
import math
from configs.config_main import *
from colors import *
from player import Player
from environment.map import world_map

# 5 : 30

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
	
	# DRAW PLAYER
	pygame.draw.circle(surface, GREEN, player.position, 12)

	player_ray = (
		player.x + WIDTH * math.cos(player.angle),
		player.y + WIDTH * math.sin(player.angle)
	)

	pygame.draw.line(surface, GREEN, player.position, player_ray)

	# DRAW MAP
	for x, y in world_map:
		pygame.draw.rect(surface, DARKGRAY, (x, y, TILE_SIZE, TILE_SIZE), 2)

	pygame.display.flip() # update display image
	clock.tick(TARGET_FPS)