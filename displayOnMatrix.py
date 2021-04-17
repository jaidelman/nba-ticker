import time
from random import randrange
import board
import terminalio
from adafruit_matrixportal.matrixportal import MatrixPortal

# --- Display Setup --- #

matrixportal = MatrixPortal(
    status_neopixel=board.NEOPIXEL,
)

FONT = "/5x8.bdf"

RED = 0x552583
RED_ALTERNATE = 0xFDB927
BLUE = 0xDB3EB1
BLUE_ALTERNATE = 0x41B6E6

RED_X = 32
RED_SHADOW_X = RED_X + 1
BLUE_X = 49
BLUE_SHADOW_X = BLUE_X + 1

# Red Score Shadow
matrixportal.add_text(
    text_font=FONT,
    text_position=(RED_SHADOW_X, int(
        matrixportal.graphics.display.height * 0.75) - 4),
    text_color=RED_ALTERNATE,
)

# Blue Score Shadow
matrixportal.add_text(
    text_font=FONT,
    text_position=(BLUE_SHADOW_X, int(
        matrixportal.graphics.display.height * 0.75) - 4),
    text_color=BLUE_ALTERNATE,
)

# Red Score
matrixportal.add_text(
    text_font=FONT,
    text_position=(RED_X, int(
        matrixportal.graphics.display.height * 0.75) - 4),
    text_color=RED,
)

# Blue Score
matrixportal.add_text(
    text_font=FONT,
    text_position=(BLUE_X, int(
        matrixportal.graphics.display.height * 0.75) - 4),
    text_color=BLUE,
)

# Red Team name shadow
matrixportal.add_text(
    text_font=FONT,
    text_position=(RED_SHADOW_X, int(
        matrixportal.graphics.display.height * 0.25) - 5),
    text_color=RED_ALTERNATE,
)

# Blue Team name shadow
matrixportal.add_text(
    text_font=FONT,
    text_position=(BLUE_SHADOW_X, int(
        matrixportal.graphics.display.height * 0.25) - 5),
    text_color=BLUE_ALTERNATE,
)

# Red Team name
matrixportal.add_text(
    text_font=FONT,
    text_position=(RED_X, int(
        matrixportal.graphics.display.height * 0.25) - 5),
    text_color=RED,
)

# Blue Team name
matrixportal.add_text(
    text_font=FONT,
    text_position=(BLUE_X, int(
        matrixportal.graphics.display.height * 0.25) - 5),
    text_color=BLUE,
)

# Temp hardcoded values
RED_SCORE = 103
BLUE_SCORE = 97
RED_ABBR = "LAL"
BLUE_ABBR = "MIA"
while True:
    matrixportal.set_text(RED_SCORE, 0)
    matrixportal.set_text(BLUE_SCORE, 1)
    matrixportal.set_text(RED_SCORE, 2)
    matrixportal.set_text(BLUE_SCORE, 3)
    matrixportal.set_text(RED_ABBR, 4)
    matrixportal.set_text(BLUE_ABBR, 5)
    matrixportal.set_text(RED_ABBR, 6)
    matrixportal.set_text(BLUE_ABBR, 7)
