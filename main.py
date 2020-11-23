import configparser
from espn_api.football import League

# Init
config = configparser.RawConfigParser()
config.read('sample.ini')
league = League(league_id=int(config["League"]["LeagueId"]),
                year=int(config["League"]["SeasonId"]),
                espn_s2=config["League"]["Espn_S2"],
                swid=config["League"]["Swid"],
                debug=True)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {league.least_scorer()}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
