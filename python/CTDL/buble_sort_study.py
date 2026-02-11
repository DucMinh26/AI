def buble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] =  arr[j+1], arr[j]
    return arr

def liner_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def  binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == target:
            return mid
        
        if target > guess :
            low = mid + 1
             

        else:
            high = mid - 1

    return -1
mang = [64, 34, 25, 12, 22, 11, 90]

print(mang)
print(binary_search(mang,12))
print(buble_sort(mang))
print(binary_search(mang,12))