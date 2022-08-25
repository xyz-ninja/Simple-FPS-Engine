import pygame
import math
from configs.config_main import *

class Player:
	
	def __init__(self):
		self.x, self.y = player_position
		self.angle = player_angle

	@property
	def position(self):
		return (self.x, self.y)

	def update_movement(self):

		sin_a = math.sin(self.angle)
		cos_a = math.cos(self.angle)

		keys = pygame.key.get_pressed()

		# translate
		if keys[pygame.K_w]:
			self.x += player_speed * cos_a
			self.y += player_speed * sin_a
			
		if keys[pygame.K_s]:
			self.x += -player_speed * cos_a
			self.y += -player_speed * sin_a

		if keys[pygame.K_a]:
			self.x += player_speed * sin_a
			self.y += -player_speed * cos_a

		if keys[pygame.K_d]:
			self.x += -player_speed * sin_a
			self.y += player_speed * cos_a

		# rotate
		if keys[pygame.K_LEFT]:
			self.angle -= 0.02
		if keys[pygame.K_RIGHT]:
			self.angle += 0.02