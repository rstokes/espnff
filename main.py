import configparser
from espn_api.football import League

# Init
config = configparser.RawConfigParser()
config.read('rob.ini')
league = League(league_id=int(config["League"]["LeagueId"]),
                year=int(config["League"]["SeasonId"]),
                espn_s2=config["League"]["Espn_S2"],
                swid=config["League"]["Swid"])


def print_team_and_roster():
    for team in league.teams:
        print(team.owner + " " + str(team.points_for))
        for player in team.roster:
            print("-- " + player.name)



print_team_and_roster()