scores = [80, 100, 70, 90, 40]

def total(scores):
    total_sum = 0
    for i in range(0, len(scores)):
        total_sum += scores[i]
    return total_sum
print(total(scores))

def avg(scores):
    total_sum = 0
    for i in range(0, len(scores)):
        total_sum += scores[i]
    total_avg = total_sum / len(scores)
    return total_avg
print(avg(scores))