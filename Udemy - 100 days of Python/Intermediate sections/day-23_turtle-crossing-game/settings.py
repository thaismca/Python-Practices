# Settings
# screen
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
FINISH_LINE_Y = (SCREEN_HEIGHT/2) - 20
SAFE_ZONE = 100

# turtle player
PLAYER_START_POSITION = (0, -(SCREEN_HEIGHT/2) + 20)
PLAYER_MOVE_PACE = 10

# cars
CAR_COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
CAR_START_MOVE_PACE = 5
CAR_MOVE_INCREMENT = 5
SPAWN_RANGE_MIN = -SCREEN_HEIGHT/2 + SAFE_ZONE
SPAWN_RANGE_MAX = SCREEN_HEIGHT/2 - SAFE_ZONE
SPAWN_INTERVAL = 10

# player and cars collision
COLLISION_RANGE = 22

# scoreboard
LEVEL_TEXT_FONT = ("Courier", 14, "bold")
LEVEL_TEXT_POSTION = (-SCREEN_WIDTH/2 + 30, SCREEN_HEIGHT/2 - 30)
GAME_OVER_TEXT_FONT = ("Courier", 24, "bold")