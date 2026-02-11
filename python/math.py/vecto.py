def cong_vector(arr1, arr2):
    if len(arr1) != len(arr2):
        return "2 vector phải cùng định dạng"
    
    tong = []

    for i in range(len(arr1)):
        tong.append(arr1[i] + arr2[i])

    return tong

def nhan_vector(arr, k):
    return [i * k for i in arr ]

def tich_vo_huong_vector(arr1, arr2):
    # if len(arr1) != len(arr2):
    #     return "2 vector phải đồng dạng"
    
    # tong = 0
    # for i in range(len(arr1)):
    #     tong +=  arr1[i]*arr2[i]

    return sum([a*b for a,b in zip(arr1, arr2)]) if len(arr1) == len(arr2) else "2 vector phải đồng dạng"

v1 = [25,170,65,0]
v2 = [1,1,1]
user_a = [10, 2, 1]
user_b = [9, 3, 2]
user_c = [1, 9, 10]

print(cong_vector(v1,v2))
print(nhan_vector(v2,2))

print(f"Độ tương đồng A và B: {tich_vo_huong_vector(user_a, user_b)}")
print(f"Độ tương đồng A và C: {tich_vo_huong_vector(user_a, user_c)}")