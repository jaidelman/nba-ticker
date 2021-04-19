import json
import requests
import teamColors
import time
import dateutil.parser
from datetime import date


def lambda_handler(event, context):
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

    payload = {}
    games = []
    for game in response['payload']['date']['games']:
        awayAbbr = game['awayTeam']['profile']['abbr']
        homeAbbr = game['homeTeam']['profile']['abbr']
        awayScore = game['boxscore']['awayScore']
        homeScore = game['boxscore']['homeScore']
        clock = game['boxscore']['periodClock']
        statusDesc = game['boxscore']['statusDesc']
        startTime = dateutil.parser.parse(game['profile']['dateTimeEt'])
        awayColors = teamColors.colors[awayAbbr]
        homeColors = teamColors.colors[homeAbbr]

        if statusDesc is not None:
            statusDesc = statusDesc.upper()
        else:
            statusDesc = startTime.strftime("%I:%M %p")

        obj = {
            'awayAbbr': awayAbbr,
            'homeAbbr': homeAbbr,
            'awayScore': awayScore,
            'homeScore': homeScore,
            'clock': clock,
            'statusDesc': statusDesc,
            'awayColors': awayColors,
            'homeColors': homeColors
        }
        games.append(obj)

    payload['payload'] = games

    # TODO implement
    return {
        'statusCode': 200,
        'body': payload
    }
