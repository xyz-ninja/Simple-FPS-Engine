from turtle import pos
import pygame
from configs.config_main import *
from environment.map import world_map
from colors import *

def cast_rays_sector(surface, position, angle, rays_count):
	current_angle = angle - HALF_FOV
	xo, yo = position

	for ray in range(rays_count):
		sin_a = math.sin(current_angle)
		cos_a = math.cos(current_angle)

		for depth in range(MAX_DEPTH):
			x = xo + depth * cos_a
			y = yo + depth * sin_a

			pygame.draw.line(surface, DARKGRAY, position, (x, y), 2)

			# simple tile collsion detection

			target_tile = (x // TILE_SIZE * TILE_SIZE, y // TILE_SIZE * TILE_SIZE)

			if target_tile in world_map:

				projection_height = PROJECTION_COEF / depth

				pygame.draw.rect(surface, WHITE,
					(ray * PROJECTION_SCALE, HALF_SCREEN_HEIGHT - projection_height // 2, PROJECTION_SCALE, projection_height)
				)

				break

		current_angle += RAYS_DELTA_ANGLE