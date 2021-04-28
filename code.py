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
def displayTime(game):
    matrixportal.set_text("", 0)
    matrixportal.set_text("", 1)
    matrixportal.set_text("", 2)
    matrixportal.set_text("", 3)
    
    # If away team is winning use their color, if home team is winning (or game hasn't started) use home color
    if game["awayScore"] > game["homeScore"]:
        matrixportal.set_text_color(game["awayColors"]["primary"], 8)
    else:
        matrixportal.set_text_color(game["homeColors"]["primary"], 8)

    # Based on the info we have display different things
    if game['statusDesc'] is not None and game['clock'] is not None:
        matrixportal.set_text(f'{game["clock"]} {game["statusDesc"]}', 8)
    elif game['statusDesc'] is not None:
        matrixportal.set_text(game["statusDesc"], 8)
    else:
        matrixportal.set_text(f'{game["awayAbbr"]} VS. {game["homeAbbr"]} - {game["startTime"]}', 8)
    matrixportal.scroll_text(SCROLL_SPEED)

# Gets the scores from our API and stores them in a data object
def getScores():
    print("Getting scores")
    gc.collect()
    response = matrixportal.fetch()
    data = json.loads(response)

    return data

# Sets the scores on the board, returns if the game has started or not
def setScore(game):
    
    # Away Name Shadow
    matrixportal.set_text(game["awayAbbr"], 4)
    matrixportal.set_text_color(game["awayColors"]["alt"], 4)
    
    # Away Name
    matrixportal.set_text(game["awayAbbr"], 6)
    matrixportal.set_text_color(game["awayColors"]["primary"], 6)
    
    # Home Name Shadow
    matrixportal.set_text(game["homeAbbr"], 5)
    matrixportal.set_text_color(game["homeColors"]["alt"], 5)
    
    # Home Name
    matrixportal.set_text(game["homeAbbr"], 7)
    matrixportal.set_text_color(game["homeColors"]["primary"], 7)
    
    if game["awayScore"] == 0 and game["homeScore"] == 0:
        return False
    else:
        # Away Score Shadow
        matrixportal.set_text(game["awayScore"], 0)
        matrixportal.set_text_color(game["awayColors"]["alt"], 0)
        
        # Away Score
        matrixportal.set_text(game["awayScore"], 2)
        matrixportal.set_text_color(game["awayColors"]["primary"], 2)
        
        # Home Score Shadow
        matrixportal.set_text(game["homeScore"], 1)
        matrixportal.set_text_color(game["homeColors"]["alt"], 1)
        
        # Home Score
        matrixportal.set_text(game["homeScore"], 3)
        matrixportal.set_text_color(game["homeColors"]["primary"], 3)
        
        return True

# Checks if there are any ongoing games, this is to set the refresh rate (we want to refresh more often if there are)
def areThereOngoingGames(data):
    # Loop through all games to see if one is going on
    for game in data['body']['payload']:
        # If the game has a score but it's not the final score, it is ongoing so return true
        if (game["awayScore"] != 0 and game["homeScore"] != 0) and game['statusDesc'] != "FINAL":
            return True
      
    # If we get though the loop without finding a game in progress we can return false
    return False

# --- Main --- #

REFRESH_RATE_DURING_GAMES = 900 # If games are going on, update scores every 15 minutes
REFRESH_RATE_OUTSIDE_GAMES = 1800 # If there are no games on, wait half an hour before checking again
data = None # Store the live data
refresh_time = None # Store time of last refresh
refresh_rate = None # Store refresh rate
i = 0 # Increment counter

while True:
    
    # If it's the first loop or it's been longer than our refresh rate, get live scores
    if (not refresh_time) or ((time.monotonic() - refresh_time) > refresh_rate):
        data = getScores()
        refresh_rate = REFRESH_RATE_DURING_GAMES if areThereOngoingGames(data) else REFRESH_RATE_OUTSIDE_GAMES # Update refresh rate (in case all games ended)
        refresh_time = time.monotonic()
        print("Refreshing in {:.0f} minutes".format(refresh_rate/60))
    
    # Display our information
    if data is not None:
        index = int(i/2) # We want to show the score/time twice before switching to the next game
        game = data['body']['payload'][index]
        gameStarted = setScore(game)
        
        # If the games started, wait 10 seconds then show the status/time
        if gameStarted: 
            time.sleep(10)
            displayTime(game)
        # If the game hasn't started, display start time twice
        else:
            displayTime(game)
            time.sleep(2)
            displayTime(game)
            time.sleep(2)
        
        # Increment index
        if i < len(data['body']['payload'])*2 - 1:
            i += 1
        else:
            i = 0
