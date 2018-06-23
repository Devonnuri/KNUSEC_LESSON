name, age = input(), int(input())

print(f'이름: {name}, 나이: {age}세')
if age < 19:
    print('출입불가')
else:
    print('출입가능')