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

# --- TEST ---
danh_sach = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91] # Đã sắp xếp
so_can_tim = 23

print("Danh sách:", danh_sach)
print(f"Vị trí số {so_can_tim} (Binary Search):", binary_search(danh_sach, so_can_tim))