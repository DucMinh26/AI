user_data = [
    [10,2,1],
    [9,3,2],
    [1,9,10]
]

def diem_user(matrix, target):
    return matrix[target]


def cong_matrix(arr1, arr2):
    tong = [];
    for i in range(len(arr1)):
        hang_moi = []
        for j in range(len(arr1[0])):
            hang_moi.append(arr1[i][j] + arr2[i][j])
        tong.append(hang_moi)
    return tong

    # return [[arr1[i][j] + arr2[i][j] for j in range(len(arr1[0]))] for i in range(len(arr1))]

def transpose(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    matrix_0 = [[0 for j in range(num_rows)] for i in range(num_cols)]
    for i in range(num_rows):
        for j in range(num_cols):
            matrix_0[j][i] = matrix[i][j]

    return matrix_0
    # return [list(a) for a in zip(*matrix)]

# Ma trận điểm thưởng
bonus_points = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]
data = [
    [10, 2, 1],
    [9, 3, 2]
]
# --- TEST ---
print("Dữ liệu gốc của User B:", diem_user(user_data, 1))
print("Ma trận sau khi cộng thưởng:")
ket_qua = cong_matrix(user_data, bonus_points)
print(ket_qua)
print("ma trận chuyển vị: ")
print(transpose(data))