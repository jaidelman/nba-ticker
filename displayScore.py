import board
import time

from adafruit_matrixportal.matrixportal import MatrixPortal
# --- Setup --- #

FONT = "/5x8.bdf"
SCROLL_SPEED = 0.04

matrixportal = MatrixPortal(
    status_neopixel=board.NEOPIXEL,
)

team_one_color = 0x552583
team_one_alternate = 0xFDB927
team_two_color = 0xBA0C2F
team_two_alternate = 0xB4975A

team_one_x = 32
team_one_shadow_x = team_one_x + 1
team_two_x = 49
team_two_shadow_x = team_two_x + 1

top_row_height = int(
    matrixportal.graphics.display.height * 0.25) - 5
bottom_row_height = int(
    matrixportal.graphics.display.height * 0.75) - 4

# --- Text Fields --- #

# Team One Score Shadow
matrixportal.add_text(
    text_font=FONT,
    text_position=(team_one_shadow_x, bottom_row_height),
    text_color=team_one_alternate,
)

# Team Two Score Shadow
matrixportal.add_text(
    text_font=FONT,
    text_position=(team_two_shadow_x, bottom_row_height),
    text_color=team_two_alternate,
)

# Team One Score
matrixportal.add_text(
    text_font=FONT,
    text_position=(team_one_x, bottom_row_height),
    text_color=team_one_color,
)

# Team Two Score
matrixportal.add_text(
    text_font=FONT,
    text_position=(team_two_x, bottom_row_height),
    text_color=team_two_color,
)

# Team One Name Shadow
matrixportal.add_text(
    text_font=FONT,
    text_position=(team_one_shadow_x, top_row_height),
    text_color=team_one_alternate,
)

# Team Two Name Shadow
matrixportal.add_text(
    text_font=FONT,
    text_position=(team_two_shadow_x, top_row_height),
    text_color=team_two_alternate,
)

# Team One Name
matrixportal.add_text(
    text_font=FONT,
    text_position=(team_one_x, top_row_height),
    text_color=team_one_color,
)

# Team Two Name
matrixportal.add_text(
    text_font=FONT,
    text_position=(team_two_x, top_row_height),
    text_color=team_two_color,
)

# Time
matrixportal.add_text(
    text_font=FONT,
    text_position=(32, bottom_row_height),
    text_color=team_one_color,
    scrolling=True
)

# Temp hardcoded values
team_one_score = "93"
team_two_score = "105"
team_one_abbr = "LAL"
team_two_abbr = "TOR"

clock_left = "11:28"
quarter = "QTR 3"


def displayTime():
    matrixportal.set_text("", 0)
    matrixportal.set_text("", 1)
    matrixportal.set_text("", 2)
    matrixportal.set_text("", 3)
    matrixportal.set_text(f'{clock_left} - {quarter}', 8)
    matrixportal.scroll_text(SCROLL_SPEED)


while True:
    matrixportal.set_text(team_one_score, 0)
    matrixportal.set_text(team_two_score, 1)
    matrixportal.set_text(team_one_score, 2)
    matrixportal.set_text(team_two_score, 3)
    matrixportal.set_text(team_one_abbr, 4)
    matrixportal.set_text(team_two_abbr, 5)
    matrixportal.set_text(team_one_abbr, 6)
    matrixportal.set_text(team_two_abbr, 7)
    time.sleep(5)
    displayTime()
