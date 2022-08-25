import math

# game
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2 # // - in python its integer division
HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2

TARGET_FPS = 60

TILE_SIZE = 100

# ray casting
FOV = math.pi / 3 # in radians, simply 60 degrees
HALF_FOV = FOV / 2
NUMBER_OF_RAYS = 120
MAX_DEPTH = 800 # max view distance
DELTA_ANGLE = FOV / NUMBER_OF_RAYS

PROJECTION_DISTANCE = NUMBER_OF_RAYS / (2 * math.tan(HALF_FOV))
PROJECTION_COEF = PROJECTION_DISTANCE * TILE_SIZE
PROJECTION_SCALE = SCREEN_WIDTH // NUMBER_OF_RAYS

# player
player_position = (HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT)
player_angle = 0
player_speed = 2