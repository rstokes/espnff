from collections import defaultdict

# This changes on Monday morning
# 1 is subtracted because until Monday the prior week is not complete
def get_num_weeks(league):
    return league.current_week - 1


def get_num_weeks_zero_index(league):
    return get_num_weeks(league) - 1


# Builds dictionary of all scores for each team
# Key is zero index week number, value is the list of scores for that week.
# {
#   0: [63.02, 66.4, 67.46, 71.4, 83.52, 93.24, 94.02, 99.5, 107.54, 109.1, 116.26, 117.18, 149.58],
#   1: [57.24, 67.76, 82.18, 85.26, 99.88, 104.06, 104.16, 117.46, 120.22, 121.78, 133.9, 135.1, 139.02],
#   2: [69.66, 75.36, 81.24, 83.38, 94.1, 94.64, 95.38, 96.8, 102.3, 108.28, 109.7, 113.52, 121.9]
# }
def build_scores(league):
    scores = defaultdict(list)
    # build map of all scores in each week
    for week in range(get_num_weeks(league)):
        for team in league.teams:
            scores[week].append(team.scores[week])
    # sort all scores
    for week in range(get_num_weeks(league)):
        # sort scores so highest score is last (highest index)
        scores[week].sort()
    return scores
