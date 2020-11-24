from collections import defaultdict


def mikrut_scale(league, team_id):
    scores = __build_scores(league)
    ranks = __get_ranks(league, scores)
    return ranks[team_id]


def __get_ranks(league, scores):
    ranks_list = defaultdict(list)
    ranks = {}
    for team in league.teams:
        for week in range(__get_num_weeks(league)):
            # find index of score in
            ranks_list[team.team_id].append(scores[week].index(team.scores[week]))

    for team_id in ranks_list:
        ranks[team_id] = sum(ranks_list[team_id])

    return ranks


def __build_scores(league):
    scores = defaultdict(list)
    # build map of all scores in each week
    for week in range(__get_num_weeks(league)):
        for team in league.teams:
            scores[week].append(team.scores[week])
    # sort all scores
    for week in range(__get_num_weeks(league)):
        scores[week].sort()
    return scores


def __get_num_weeks(league):
    return len(league.teams[0].scores)
