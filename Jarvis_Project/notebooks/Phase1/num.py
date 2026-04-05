import numpy as np
np.set_printoptions(precision=1, suppress=True)

# zero = np.zeros((3,4))
# one = np.ones((2,5))
# ran = np.arange(10,51)

# wei = np.array([65, 70, 75, 80, 85])
# heig = np.array([1.7, 1.75, 1.8, 1.65, 1.85])
# bmi = wei / (heig ** 2)

# mask = (bmi >= 25)

# fat_bmi = np.round(bmi[mask],2)


# mang_1D = np.array([8, 7, 9, 5, 6, 7, 9, 9, 10])
# mang_3x3 = mang_1D.reshape(3,3)

# print("mang moi: \n", mang_3x3)
# print("hs thu 2: ", mang_3x3[1,:])
# print("diem ly: ", mang_3x3[:,1])

# mang_2x2 = mang_3x3[0:2,0:2]
# print(mang_2x2)

# print("diem trung binh tung hs: ", np.round(np.mean(mang_3x3, axis=1),2))
# tb_mon = np.mean(mang_3x3, axis=0)
# mon_kho = np.min(tb_mon)

# index_mon_kho = np.argmin(mon_kho)
# print("mon kho nhat: ", np.round(mon_kho,2),", la mon thu: ",index_mon_kho)

# mask_diem_cao = (mang_3x3 >= 9)
# print(mask_diem_cao)
# so_mon_gioi = np.sum(mask_diem_cao, axis=1)
# print("Số môn đạt điểm >= 9 của từng học sinh:", so_mon_gioi)

# diem_thi = np.array([
#     [8.0, 7.0, 9.0],
#     [5.0, 6.0, 7.0],
#     [9.0, 9.0, 9.5]
# ])

# diem_cong = np.array([1.0, 0.5, 0.5])
# ket_qua = diem_thi + diem_cong
# print(ket_qua)

# np.clip(ket_qua, a_min= 0, a_max= 10, out=ket_qua)
# # np.clip(ket_qua,0,10,ket_qua)
# print(ket_qua)

don_gia = np.array([50, 30, 20])
gio_hang = np.array([
    [2, 1, 0],
    [0, 3, 5],
    [1, 1, 1]
])


tong_tien = gio_hang @ don_gia
print(tong_tien)