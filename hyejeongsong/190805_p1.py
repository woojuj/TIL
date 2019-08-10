scores = [80,100,70,90,40]

def total_score():
    return sum(scores)

print("Total score:", total_score())

def avg_score():
    return total_score() / len(scores)
print("Average score:", avg_score())