from configs.config_main import *

text_map = [
	"WWWWWWWWWWWWWW",
	"W............W",
	"W............W",
	"W............W",
	"W............W",
	"W............W",
	"W............W",
	"WWWWWWWWWWWWWW",
]

world_map = set()

for j, row in enumerate(text_map):
	for i, char in enumerate(row):
		if char == "W":
			wall_position = (i * TILE_SIZE, j * TILE_SIZE)
			world_map.add(wall_position)