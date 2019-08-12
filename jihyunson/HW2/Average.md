## 성적 총합 & 평균 구하기

my_scores = [30, 90, 80, 40, 50]

class_scores = [
    [30, 90, 80, 40, 50],
    [100, 100, 100, 100, 100],
    [90, 90, 30, 30, 20]
]

1. First try: name 'total' is not defined
```py
def test_total():
    assert total([80]) == 80
```

2. Second try: total( ) takes 0 positional arguments but 1 was given
```py
def total():
    pass

def test_total():
    assert total([80]) == 80
```

3. Third try: assert None == 80
```py
def total(scores):
    pass

def test_total():
    assert total([80]) == 80
```

4. Fourth try
```py
def total(scores):
    return 80

def test_total():
    assert total([80]) == 80
```

5. Fifth try: PASSED
```py
def total(scores):
    return scores[0]

def test_total():
    assert total([80]) == 80
```

6. Sixth try: 80 != 180
```py
def total(scores):
    return scores[0]

def test_total():
    assert total([80]) == 80
    assert total([80, 100]) == 180
```
