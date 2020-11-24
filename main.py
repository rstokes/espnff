import configparser
from espn_api.football import League
from mikrut_scale import mikrut_scale
from strength_of_schedule import average_points_against
from lib import get_num_weeks
from datetime import datetime

# Init
config = configparser.RawConfigParser()
config.read('rob.ini')
league = League(league_id=int(config["League"]["LeagueId"]),
                year=int(config["League"]["SeasonId"]),
                espn_s2=config["League"]["Espn_S2"],
                swid=config["League"]["Swid"])


def main():
    print("Reporting data through week " + str(get_num_weeks(league)) + " as of " + str(datetime.now().strftime("%m/%d/%Y %I:%M %p")))
    print("Team, Mikrut Scale, Average Points Against")
    for team in league.teams:
        print(team.owner + ", " + str(mikrut_scale(league, team.team_id)) + ", " + str(average_points_against(league, team.team_id)))
        #print(team.owner + " " + str(team.points_for))
        # for player in team.roster:
        #     print("-- " + player.name)

main()