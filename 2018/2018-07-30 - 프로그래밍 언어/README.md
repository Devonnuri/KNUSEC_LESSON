# Python Programming

## 표준 모듈
거의 모든 기능들이 포함되어 있다.

### 시간

#### time() : 현재 시간을 반환한다. (Unix Timestamp)
#### 카운트다운
```python
import time

for i in range(10, 0, -1):
    print(i)
    time.sleep(1)

print('Fire!!')
```

### 난수

#### random() : 0~1 사이의 실수를 반환한다.
```python
import random

print(random.random()) # 0 ~ 1 사이의 실수를 출력한다.
print(random.random()*5) # 0 ~ 5 사이의 실수를 출력한다.
```
#### randint(a, b) : a, b사이의 수를 반환한다.

#### 별 랜덤하게 출력하기
```python
import random

while True:
    for i in range(random.randint(0, 40)):
        print('*', end='')
    print()
```

#### 과제 1. 로또 중복 안나오게 하기
* 출제자가 원하는 답
```python
import random

pnu = []
count = 0
while True:
    nu = random.randint(1, 45)
    if nu not in pnu:
      pnu.append(nu)
```

* 위에서 최적화한 답
```python
import random

pnu = []
while len(pnu) < 6:
    nu = random.randint(1, 45)
    if nu not in pnu:
        print(nu)
        pnu.append(nu)
```

* 세줄 ~~헨타이~~ 코딩
```python
a = [str(i) for i in range(1, 45)]
__import__('random').shuffle(a)
print('\n'.join(a[:6]))
```