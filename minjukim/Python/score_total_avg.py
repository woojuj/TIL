def total(l):
    total_score = 0
    for score in l:
        total_score += score
    return total_score

def average(l):
    avg_score = total(l) / len(l)
    return avg_score

scores = [80, 100, 70, 90, 40]
print(total(scores))
print(average(scores))
