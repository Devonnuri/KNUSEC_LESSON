# Python Programming

http://learnpython.org/

이 사이트에서 주로 진행되었다.

## 코드 블럭
파이썬은 코드블럭을 기준으로 구분을 하기 때문에 코드블럭이 굉장히 중요하다.

(PEP 기준에는 4 space가 indentation의 기준이다.)

## 변수

값을 저장하는 공간이다.

파이썬의 변수는 정해진 type이 없다. (Weak typed language지만 Javascript보다는 Strict하다)

문자열은 `"string"` `'string'` 이렇게 나타낼 수 있다. (C와는 달리 둘의 역할이 같음)

## 연산

### 사칙 연산

```python
number = 1 + 2 * 3 / 4.0
print(number)
```

### mod 연산(나머지)

```python
remainder = 11 % 3
print(remainder)
```

### 거듭제곱(power) 연산

```python
squared = 7 ** 2
cubed = 2 ** 3
```

### 문자열 더하기

```python
helloworld = "Hello" + " " + "world"
print(helloworld)
```

### 문자열 곱하기

```python
lotsofhellos = "hello" * 5
print(lotsofhellos) # result: hellohellohellohellohello
```

## 리스트

### 추가

```python
mylist = [1, 2, 3, 4]
mylist.append(5)
```

### pop

```python
mylist = [1, 2, 3, 4, 5]
mylist.pop() # result: 5
```

### insert

```python
mylist = [1, 3, 4, 5]
mylist.insert(1, 2) # 1번 위치에 2를 끼워넣음
print(mylist) # result: [1, 2, 3, 4, 5]
```

### 값 가져오기

**배열의 인덱스는 0부터 시작한다**

```python
mylist = [1, 2, 3, 4, 5]
print(mylist[2]) # result: 3
```

### 리스트끼리 연산

> PPT에는 `리스트끼리 더하기, 빼기`로 되었으나 list 끼리의 빼기 연산은 불가능하다.

```python
even_numbers = [2, 4, 6, 8]
odd_numbers = [1, 3, 5, 7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)
```

## Format String

```
%s - 문자열
%d - 정수
%f - 부동소수점 실수
%.<자리수>f - 자리수 만큼으로 반올림한 실수
%x/%x - 16진수로 출력한다(소문자/대문자) 
```

```python
name = "John"
age = 23
print("%s is %d years old" % (name, age))
```

## 배열/문자열 관련 함수

여기에서 다루는 함수들은 배열과 문자열 모두에 적용될 수 있다.

### 길이

```python
arr = [1, 2, 3, 4, 5]
print(len(arr)) # result: 5

hello = "helloworld"
print(len(hello)) # result: 10
```

### 값의 위치

```python
astring = "Hello world!"
print(astring.index("o")) # result: 4
```

### 값의 개수

```python
astring = "Hello world!"
print(astring.count("l")) # result: 3
```

### 범위 선택

#### 처음과 끝

```python
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(astring[3:7]) # result: [4, 5, 6, 7]
```

#### 처음과 끝과 간격

```python
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(astring[2:8:2]) # result: [3. 5, 7]
```

#### 범위나 간격이 음수일 때
* 범위가 음수일 때 : 반대쪽
* 간격이 음수일 때 : 반대 방향

#### 예제 1: 0~9의 문자열이 있을때 642가 출력 되도록 해라
```python
print(''.join(map(str, range(10)))[2:8:-2])
```

#### 예제 2: 0~9의 문자열이 있을때 901가 출력 되도록 해라
> 교수님: 해봐
> 
> (... 아무도 못한다)
>
> 교수님: 안되는 구나.. 미안하다

안되는거다. ㅇㅇ

## 문자열 함수
### 대문자, 소문자
```python
astring = "Hello World!"
print(astring.upper()) # result: HELLO WORLD!
print(astring.lower()) # result: hello world!
```

### 나누기
```python
astring = "Hello World!"
print(astring.split(" "))
```

## 과제 1: 이름과 나이를 입력 받아서 한줄에
```python
print(f'이름: {input()}, 나이: {input()}세')
```

## 조건: True or False 반환
* `==`: 같은가?
* `<`, `>`, `<=`, `>=`: 작은가? 큰가? 작거나 같은가? 크거나 같은가?

```python
x = 2
print(x == 2) # result: True
print(x == 3) # result: False
print(x < 3) # result: True
```
* in: 포함 여부

```python
name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")
```

## if 문:
```python
x = 3
if x == 2:
    print('x는 2다!')
elif x == 3:
    print('x는 3이다!')
else:
    print('x는 2도 3도 아니다!')
```

## 과제 2
> 과제 1에서 나이가 19 이상이면 "출입가능" 아니면 "출입불가"를 출력하시오

```python
name, age = input(), input()

print(f'이름: {name}, 나이: {age}세')
if age < 19:
    print('출입불가')
else:
    print('출입가능')
```

## 과제 3
> 숫자를 입력받아 아래 numbers 에서 찾고, 찾으면 "있음", 못찾으면 "없음"을 출력하는 프로그램
>
> `numbers = [1, 3, 6, 2, 3, 6, 2134, 34, 3245]`

* 방법 1. in을 사용하는 방법
```python
print("있음" if int(input()) in [1, 3, 6, 2, 3, 6, 2134, 34, 3245] else "없음")
```

* 방법 2. 간단히 순회하는 방법
```python
arr = [1, 3, 6, 2, 3, 6, 2134, 34, 3245]

num = int(input())
flag = False

for i in arr:
    if num == i:
        flag = True
        break

print('있음' if flag else '없음')
```

* 방법 3. 이진 탐색
```python
def binarySearch(arr, item):
    first = 0
    last = len(arr) - 1
    
    if len(arr) == 0:
        return '없음'
    else:
        i = (first + last) // 2
        if item == arr[i]:
            return '있음'
        else:
            if arr[i] < item:
                return binarySearch(arr[i+1:], item)
            else:
                return binarySearch(arr[:i], item)

arr = [1, 3, 6, 2, 3, 6, 2134, 34, 3245]
print(binarySearch(arr, int(input())))
```

## 과제 4
> 구구단 출력
* 방법 1. 정상적인 방법
```python
for i in range(2, 10):
    print(f'{i}단\n')
    for j in range(1, 10):
        print(f'{i} * {j} = {i*j}')
    print('\n')
```
* 방법 2. 변태같은 방법
```python
'\n\n'.join(map(lambda x: '\n'.join(map(lambda y: f'{x} * {y} = {x*y}', range(1, 10))), range(2, 10)))
```

## 과제 5
> 전화번호 검색 프로그램
> 
> 이름을 입력받아서 전화번호를 출력
> 
> 없으면 없음을 출력

```python
phonebook = {
    "John": 938477566,
    "Jim": 938377264,
    "Jill": 947662781
}

name = input()
if name in phonebook:
    print(phonebook[name])
else:
    print('없음')
```