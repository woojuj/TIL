scores = [80, 100, 70, 90, 40]

def total(scores):
    accumulator = 0
    for i in range(0, len(scores)):
        accumulator += scores[i]
    return accumulator

def test_total():
    assert total([80]) == 80
    assert total([80, 20]) == 100
    assert total([80, 20, 70, 80]) == 250

def average(scores):
    return total(scores) / len(scores)

def test_average():
    assert average([80]) == 80
    assert average([80, 20]) == 50