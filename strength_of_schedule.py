from lib import get_num_weeks

def average_points_against(league, team_id):
    team = next(team for team in league.teams if team.team_id == team_id)
    return round(team.points_against / get_num_weeks(league), 1)

def average_points_for(league, team_id):
    team = next(team for team in league.teams if team.team_id == team_id)
    return round(team.points_for / get_num_weeks(league), 1)



