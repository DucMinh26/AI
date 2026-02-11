import time

# 1. Tạo dữ liệu giả lập (10 triệu con số)
print("Đang tạo dữ liệu (10 triệu phần tử)... Đợi chút nhé!")
data_list = list(range(10_000_000))  # List bình thường
data_set = set(data_list)            # Set (tương tự Dictionary, dùng Hash Map)

target = 9_999_999 # Số nằm ở cuối cùng (trường hợp xấu nhất)

# --- THÍ NGHIỆM 1: Tìm kiếm kiểu O(n) ---
# Cách dùng vòng lặp hoặc toán tử 'in' trên List
start_time = time.time()

is_found = target in data_list # Python phải duyệt từ đầu đến cuối list

end_time = time.time()
print(f"1. Tìm trong LIST (O(n)): Mất {end_time - start_time:.6f} giây")

# --- THÍ NGHIỆM 2: Tìm kiếm kiểu O(1) ---
# Cách dùng Set hoặc Dictionary
start_time = time.time()

is_found = target in data_set # Nhảy dù thẳng vào vị trí cần tìm

end_time = time.time()
print(f"2. Tìm trong SET (O(1)):  Mất {end_time - start_time:.6f} giây")

# --- KẾT LUẬN ---
print("-" * 30)
print("Bạn thấy sự khác biệt chưa? Hãy tưởng tượng đây là dữ liệu khách hàng của bạn.")