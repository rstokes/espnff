from collections import defaultdict
from lib import get_num_weeks, build_scores


def mikrut_scale(league, team_id):
    scores = build_scores(league)
    ranks = __get_ranks(league, scores)
    return ranks[team_id]


# 0 points for last place in a week
# number of teams - 1 points are awarded to each weeks winner
def __get_ranks(league, scores):
    ranks_list = defaultdict(list)
    ranks = {}
    for team in league.teams:
        for week in range(get_num_weeks(league)):
            # find index of score in week
            ranks_list[team.team_id].append(scores[week].index(team.scores[week]))

    print(ranks_list)
    for team_id in ranks_list:
        ranks[team_id] = sum(ranks_list[team_id])

    return ranks
