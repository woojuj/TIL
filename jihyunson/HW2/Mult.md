## 구구단 출력하기
for i in range(2,10):
   for j in range(1, 10):
       print(i, "x", j, "=", i*j)
   print("-"*20)

1. Empty suite
```py
def mult(n):
    pass
```

2. N is note defined
```py
def mult(n):
    for i in range(2, 3):
        print (n)

def test_mult():
    assert mult(n) == 2
```

3. Passed
```py
for i in range(1, 3):
    for j in range(1, 3):
        n = i*j
        print (i*j)

def test_mult():
    assert n == 4
```

4. 
```py
for i in range(1, 10):
    for j in range(1, 10):
        n = i*j
        print (i "x" j " is " n)
```