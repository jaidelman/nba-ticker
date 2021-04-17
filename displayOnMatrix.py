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

RED = 0xFF0000
RED_ALTERNATE = 0x641690
BLUE = 0x0000FF
BLUE_ALTERNATE = 0xE46F19

# Red Score Shadow
matrixportal.add_text(
    text_font=FONT,
    text_position=(33, int(matrixportal.graphics.display.height * 0.75) - 4),
    text_color=RED_ALTERNATE,
)

# Blue Score Shadow
matrixportal.add_text(
    text_font=FONT,
    text_position=(51, int(matrixportal.graphics.display.height * 0.75) - 4),
    text_color=BLUE_ALTERNATE,
)

# Red Score
matrixportal.add_text(
    text_font=FONT,
    text_position=(32, int(matrixportal.graphics.display.height * 0.75) - 4),
    text_color=RED,
)

# Blue Score
matrixportal.add_text(
    text_font=FONT,
    text_position=(50, int(matrixportal.graphics.display.height * 0.75) - 4),
    text_color=BLUE,
)

# Red Team name shadow
matrixportal.add_text(
    text_font=FONT,
    text_position=(33, int(matrixportal.graphics.display.height * 0.25) - 5),
    text_color=RED_ALTERNATE,
)

# Blue Team name shadow
matrixportal.add_text(
    text_font=FONT,
    text_position=(51, int(matrixportal.graphics.display.height * 0.25) - 5),
    text_color=BLUE_ALTERNATE,
)

# Red Team name
matrixportal.add_text(
    text_font=FONT,
    text_position=(32, int(matrixportal.graphics.display.height * 0.25) - 5),
    text_color=RED,
)

# Blue Team name
matrixportal.add_text(
    text_font=FONT,
    text_position=(50, int(matrixportal.graphics.display.height * 0.25) - 5),
    text_color=BLUE,
)

# Temp hardcoded values
while True:
    matrixportal.set_text("103", 0)
    matrixportal.set_text("99", 1)
    matrixportal.set_text("103", 2)
    matrixportal.set_text("99", 3)
    matrixportal.set_text("TOR", 4)
    matrixportal.set_text("ORL", 5)
    matrixportal.set_text("TOR", 6)
    matrixportal.set_text("ORL", 7)
