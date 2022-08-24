import pygame
from configs.config_main import *

class Player:
	
	def __init__(self):
		self.x, self.y = player_position
		self.angle = player_angle

	@property
	def position(self):
		return (self.x, self.y)

	def update_movement(self):
		keys = pygame.key.get_pressed()

		# translate
		if keys[pygame.K_w]:
			self.y -= player_speed
		if keys[pygame.K_s]:
			self.y += player_speed

		if keys[pygame.K_a]:
			self.x -= player_speed
		if keys[pygame.K_d]:
			self.x += player_speed

		# rotate
		if keys[pygame.K_LEFT]:
			self.angle -= 0.02
		if keys[pygame.K_RIGHT]:
			self.angle += 0.02