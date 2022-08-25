import pygame
import math
from configs.config_main import *
from colors import *
from player import Player
from environment.map import world_map
from raycasting import *

pygame.init()
surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

player = Player()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()

	player.update_movement()

	surface.fill(BLACK)
	
	# DRAW PLAYER
	pygame.draw.rect(surface, BLACK, (0, 0, SCREEN_WIDTH, HALF_SCREEN_HEIGHT))
	pygame.draw.rect(surface, DARKGRAY, (0, HALF_SCREEN_HEIGHT, SCREEN_WIDTH, HALF_SCREEN_HEIGHT))

	cast_rays_sector(surface, player.position, player.angle, NUMBER_OF_RAYS)

	player_ray = (
		player.x + SCREEN_WIDTH * math.cos(player.angle),
		player.y + SCREEN_WIDTH * math.sin(player.angle)
	)

	#pygame.draw.circle(surface, GREEN, (int(player.x), int(player.y)), 12)
	#pygame.draw.line(surface, GREEN, player.position, player_ray)

	# DRAW MAP
	#for x, y in world_map:
	#	pygame.draw.rect(surface, DARKGRAY, (x, y, TILE_SIZE, TILE_SIZE), 2)

	pygame.display.flip() # update display image
	clock.tick(TARGET_FPS)