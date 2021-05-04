def latest(scores):
    return scores[-1]


def personal_best(scores):
    scores.sort(reverse=True)
    return scores[0]


def personal_top_three(scores):
    scores.sort(reverse=True)
    if len(scores) < 3:
        return scores
    result = []
    result.append(scores[0])
    result.append(scores[1])
    result.append(scores[2])
    return result
