scores = [80, 100, 70, 90, 40]

# 총합 구하기
def total(list):
    total_score=0
    for i in range(0, len(list)):
        total_score += list[i]
    return total_score

print(total(scores))

# total 함수 다시 활용하기

def average(list):
    return total(list)/len(list)

print(average(scores))

# total 함수 활용하지 않고 Average 함수 만들기
'''
def average(list):
    total_score = 0
    for i in range(0, len(list)):
        total_score += list[i]
    return total_score/len(list)

print(average(scores))
'''