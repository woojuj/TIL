def total(list):
    total_score = 0
    for score in list:
        total_score += score
    return total_score

def average(list):
    total_score = 0
    for score in list:
        total_score += score
    avg_score = total_score / len(list)
    return avg_score

scores = [80, 100, 70, 90, 40]
print(total(scores))
print(average(scores))
