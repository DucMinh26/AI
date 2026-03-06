import math

def mean(data):
    return (sum(data)/len(data))

def variance(data):
    mu = mean(data)

    sai_so_binh_phuong = [(x - mu)**2 for x in data]

    return (sum(sai_so_binh_phuong)/len(data))

def stad(data):
    v = variance(data)
    return math.sqrt(v)

def chuan_hoa_z_score(data):
    m = mean(data)
    s = stad(data)

    if s == 0:
        return [0.0 for i in data]

    return [(x - m ) / s for x in data ]

# --- TEST ---
# # Giả sử đây là điểm đánh giá mức độ thích Python của User Jarvis
# diem_so_thich = [10, 2, 1, 9, 3, 2, 1, 9, 10]

# m = mean(diem_so_thich)
# var = variance(diem_so_thich)
# std = stad(diem_so_thich)

# print(f"Dữ liệu: {diem_so_thich}")
# print(f"1. Giá trị trung bình (Mean): {m:.2f}")
# print(f"2. Phương sai (Variance): {var:.2f}")
# print(f"3. Độ lệch chuẩn (Std Dev): {std:.2f}")

diem_cu = [10, 2, 1, 9, 3, 2, 1, 9, 10]
diem_moi = chuan_hoa_z_score(diem_cu)
print(mean(diem_cu))
print(stad(diem_cu))

print(f"Dữ liệu gốc: {diem_cu}")
print(f"Dữ liệu đã chuẩn hóa: {[round(d,2) for d in diem_moi]}")

# Kiểm tra thử: Tính Mean của diem_moi xem có xấp xỉ bằng 0 không?
print(f"Mean mới: {mean(diem_moi):.2f}")