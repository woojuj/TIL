scores = [80, 100, 70, 90, 40]


def total(s):
    total_score = 0
    for score in s:
        total_score += score
    return total_score


print(total(scores))


def average(s):
    average = total(s) / len(s)
    return average


print(average(scores))