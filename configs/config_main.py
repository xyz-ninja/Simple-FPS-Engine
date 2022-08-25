import math

# game
WIDTH = 1200
HEIGHT = 800

HALF_WIDTH = WIDTH // 2 # // - in python its integer division
HALF_HEIGHT = HEIGHT // 2

TARGET_FPS = 60

TILE_SIZE = 100

# ray casting
FOV = math.pi / 3 # in radians, simply 60 degrees
HALF_FOV = FOV / 2
NUMBER_OF_RAYS = 20
MAX_DEPTH = 800 # max view distance
DELTA_ANGLE = FOV / NUMBER_OF_RAYS

# player
player_position = (HALF_WIDTH, HALF_HEIGHT)
player_angle = 0
player_speed = 2