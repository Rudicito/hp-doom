import umath as math
from vector2 import Vector2 as vec2

DOOM_RES = DOOM_W, DOOM_H = 320, 200

SCALE = 1
WIN_RES = WIDTH, HEIGHT = int(DOOM_W * SCALE), int(DOOM_H * SCALE)
H_WIDTH, H_HEIGHT = WIDTH // 2, HEIGHT // 2

FOV = 90.0
H_FOV = FOV / 2

PLAYER_SPEED = 0.05
PLAYER_ROT_SPEED = 0.2
PLAYER_HEIGHT = 41

SCREEN_DIST = H_WIDTH / math.tan(math.radians(H_FOV))

COLOR_KEY = (152, 0, 136)