scores = [80, 100, 70, 90, 40]
# total
def total(list):
    return sum(list)
print("total:",total(scores))

# average
def average(sum, list):
    return sum/len(list)
# print("average:",average(scores))
print(average(total(scores), scores))