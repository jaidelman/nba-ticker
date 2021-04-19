import board
import busio
import time
import gc
import json
from adafruit_matrixportal.matrixportal import MatrixPortal

try:
    from secrets import secrets
except ImportError:
    print("WiFi secrets are kept in secrets.py, please add them there!")
    raise

# --- Constants --- #

# Board related variables
FONT = "/5x8.bdf"
SCROLL_SPEED = 0.04

# Request related variables
URL = secrets['aws-api-url']
HEADERS = {
    'x-api-key': secrets['x-api-key']
}
    
# --- MatrixPortal --- #

matrixportal = MatrixPortal(
    status_neopixel=board.NEOPIXEL,
    url=URL,
    headers=HEADERS
)

# --- (X,Y) related constants --- #

TEAM_ONE_X = 32
TEAM_ONE_SHADOW_X = TEAM_ONE_X + 1
TEAM_TWO_X = 49
TEAM_TWO_SHADOW_X = TEAM_TWO_X + 1

TOP_ROW_HEIGHT = int(
    matrixportal.graphics.display.height * 0.25) - 5
BOTTOM_ROW_HEIGHT = int(
    matrixportal.graphics.display.height * 0.75) - 4

# --- Text Fields --- #

# Team One Score Shadow
matrixportal.add_text(
    text_font=FONT,
    text_position=(TEAM_ONE_SHADOW_X, BOTTOM_ROW_HEIGHT)
)

# Team Two Score Shadow
matrixportal.add_text(
    text_font=FONT,
    text_position=(TEAM_TWO_SHADOW_X, BOTTOM_ROW_HEIGHT)
)

# Team One Score
matrixportal.add_text(
    text_font=FONT,
    text_position=(TEAM_ONE_X, BOTTOM_ROW_HEIGHT)
)

# Team Two Score
matrixportal.add_text(
    text_font=FONT,
    text_position=(TEAM_TWO_X, BOTTOM_ROW_HEIGHT)
)

# Team One Name Shadow
matrixportal.add_text(
    text_font=FONT,
    text_position=(TEAM_ONE_SHADOW_X, TOP_ROW_HEIGHT)
)

# Team Two Name Shadow
matrixportal.add_text(
    text_font=FONT,
    text_position=(TEAM_TWO_SHADOW_X, TOP_ROW_HEIGHT)
)

# Team One Name
matrixportal.add_text(
    text_font=FONT,
    text_position=(TEAM_ONE_X, TOP_ROW_HEIGHT)
)

# Team Two Name
matrixportal.add_text(
    text_font=FONT,
    text_position=(TEAM_TWO_X, TOP_ROW_HEIGHT)
)

# Time
matrixportal.add_text(
    text_font=FONT,
    text_position=(TEAM_ONE_X, BOTTOM_ROW_HEIGHT),
    scrolling=True
)

# --- Functions --- #

# Replaces the score with the time and quarter and scrolls
# the time across the board
def displayTime(index):
    game = data['body']['payload'][index]
    matrixportal.set_text("", 0)
    matrixportal.set_text("", 1)
    matrixportal.set_text("", 2)
    matrixportal.set_text("", 3)
    
    if game['statusDesc'] is not None:
        matrixportal.set_text(f'{game["clock"]} {game["statusDesc"]}', 8)
    else:
        matrixportal.set_text(f'{game["awayAbbr"]} VS. {game["homeAbbr"]} - {game["startTime"]}', 8)
    matrixportal.scroll_text(SCROLL_SPEED)

# Gets the scores from our API and stores them in a data object
def getScores():
    gc.collect()
    response = matrixportal.fetch()
    data = json.loads(response)

    return data    

# Sets the scores on the board
def setScore(index):
    game = data['body']['payload'][index]
    matrixportal.set_text(game["awayScore"], 0) # Away Score Shadow
    matrixportal.set_text(game["awayScore"], 2) # Away Score
    matrixportal.set_text(game["homeScore"], 1) # Home Score Shadow
    matrixportal.set_text(game["homeScore"], 3) # Home Score
    matrixportal.set_text(game["awayAbbr"], 4)  # Away Name Shadow
    matrixportal.set_text(game["awayAbbr"], 6)  # Away Name
    matrixportal.set_text(game["homeAbbr"], 5)  # Home Name Shadow
    matrixportal.set_text(game["homeAbbr"], 7)  # Home Name

# Im doing this to avoid having to import more libraries, saving necessary memory
# We can 'await' by using `if data is not None:` in our loop
data = None
data = getScores()

while True:
    if data is not None:
        setScore(0)
        time.sleep(5)
        displayTime(0)