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

			#pygame.draw.line(surface, DARKGRAY, position, (x, y), 2)

			# simple tile collsion detection
			target_tile = (x // TILE_SIZE * TILE_SIZE, y // TILE_SIZE * TILE_SIZE)
			if target_tile in world_map:

				# fix "fish eye effect"
				depth *= math.cos(angle - current_angle)

				projection_height = PROJECTION_COEF / depth
				
				c = 255 / (1 + depth * depth * 0.0001)
				projection_color = (c, c, c)

				pygame.draw.rect(surface, projection_color,
					(ray * PROJECTION_SCALE, HALF_SCREEN_HEIGHT - projection_height // 2, PROJECTION_SCALE, projection_height)
				)

				break

		current_angle += RAYS_DELTA_ANGLE