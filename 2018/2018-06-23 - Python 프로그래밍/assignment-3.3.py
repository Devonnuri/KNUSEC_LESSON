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