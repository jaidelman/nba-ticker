import requests

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

    print(f'{awayAbbr}: {awayScore}, {homeAbbr}: {homeScore} - {clock} {statusDesc}')
