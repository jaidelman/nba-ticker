import requests
import time
import dateutil.parser
from datetime import date

url = "https://ca.global.nba.com/stats2/scores/daily.json?countryCode=CA&locale=en&tz=-5"
headers = {
    "User-Agent ": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
    "Content-Type": "application/json;charset=UTF-8",
    "Accept": "*/*",
    "Accept-ranges": "bytes",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://www.ca.global.nba.com/"
}
response = requests.get(url=url, params=headers).json()

for game in response['payload']['date']['games']:
    awayAbbr = game['awayTeam']['profile']['abbr']
    homeAbbr = game['homeTeam']['profile']['abbr']
    awayScore = game['boxscore']['awayScore']
    homeScore = game['boxscore']['homeScore']
    clock = game['boxscore']['periodClock']
    statusDesc = game['boxscore']['statusDesc']
    startTime = dateutil.parser.parse(game['profile']['dateTimeEt'])

    if statusDesc is not None:
        print(
            f'{awayAbbr}: {awayScore}, {homeAbbr}: {homeScore} - {clock} {statusDesc}')
    else:
        print(f'{awayAbbr} VS. {homeAbbr} - {startTime.strftime("%I:%M %p")}')

    # Idea: Grab scores between 5-12pm, otherwise show yesterday's scores/upcoming games (which we don't need to ping for)
    # - If all games haven't started, don't ping until the next hour
