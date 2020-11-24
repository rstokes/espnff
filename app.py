import configparser
from espn_api.football import League
from mikrut_scale import mikrut_scale
from strength_of_schedule import average_points_against, average_points_for
from lib import get_num_weeks
from datetime import datetime

# Init
config = configparser.RawConfigParser()
config.read('rob.ini')
league = League(league_id=int(config["League"]["LeagueId"]),
                year=int(config["League"]["SeasonId"]),
                espn_s2=config["League"]["Espn_S2"],
                swid=config["League"]["Swid"])

def get_stats():
    stats = {}
    league.refresh()
    print("Reporting data through week " + str(get_num_weeks(league)) + " as of " + str(
        datetime.now().strftime("%m/%d/%Y %I:%M %p")))
    print(", ".join(["Team", "ESPN Standing", "Mikrut Scale", "Average Points Against", "Average Points For", "Wins", "Losses"]))
    for team in league.teams:
        values = [team.owner, str(team.standing), str(mikrut_scale(league, team.team_id)), str(
            average_points_against(league, team.team_id)), str(average_points_for(league, team.team_id)), str(team.wins), str(team.losses)]
        print(", ".join(values))
    return stats

get_stats()