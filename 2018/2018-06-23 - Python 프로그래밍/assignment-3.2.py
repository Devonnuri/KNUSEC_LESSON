arr = [1, 3, 6, 2, 3, 6, 2134, 34, 3245]

num = int(input())
flag = False

for i in arr:
    if num == i:
        flag = True
        break

print('있음' if flag else '없음')