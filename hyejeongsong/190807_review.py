# sum
def total(scores):
    total_score = 0
    for i in range(0,len(scores)):
            total_score += scores[i]
    return total_score

print(total([80,100,70,90,40]))

# 같은 이름은 사용하지 않는 것이 좋음
