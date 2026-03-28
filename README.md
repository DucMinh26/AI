# 🤖 Project Jarvis - AI & Project Management System

Dự án nghiên cứu và ứng dụng Machine Learning vào hệ thống quản lý dự án (6-month roadmap).

## 📅 Lộ trình cập nhật (Day 50 - 54)

Trong giai đoạn này, mình tập trung vào bài toán **Phân loại (Classification)**: Dự đoán khả năng khách hàng mua xe dựa trên Tuổi và Lương.

### 🧠 Các thuật toán đã thực nghiệm:

1. **Logistic Regression**: Tìm ranh giới tuyến tính bằng toán học.
2. **KNN (K-Nearest Neighbors)**: Phân loại dựa trên "hàng xóm" gần nhất.
3. **Decision Tree**: Xây dựng sơ đồ tư duy If/Else tự động.
4. **Random Forest**: Sử dụng sức mạnh tập thể từ 100 cây quyết định.

### 📊 Bảng so sánh hiệu suất (Kết quả thực tế)

| Thuật toán                  | Accuracy (Độ chính xác) | Ghi chú                                       |
| :---------------------------- | :-------------------------- | :--------------------------------------------- |
| **Logistic Regression** | 100.00%                     | Rất tốt với dữ liệu tuyến tính sạch.   |
| **KNN (K=3)**           | 95.00%                      | Bị ảnh hưởng bởi khoảng cách dữ liệu. |
| **Decision Tree**       | 95.00%                      | Dễ hiểu nhưng dễ bị Overfitting.          |
| **Random Forest**       | 95.00%                      | Ổn định nhất trên dữ liệu thực tế.    |

## 🛠 Công nghệ sử dụng

* [ ] **Ngôn ngữ:** Python 3.x
* [ ] **Thư viện AI:** `scikit-learn`, `pandas`, `numpy`.
* [ ] **Trực quan hóa:** `matplotlib`, `seaborn`.
* [ ] **Quản lý phiên bản:** `Git` & `GitHub`.

## 🚀 Cách chạy dự án

1. Clone repo: `git clone https://github.com/YourUsername/Neuro-sama.git`
2. Cài đặt thư viện: `pip install -r requirements.txt`
3. Chạy file main: `python main.py`

## 🚀 Giai đoạn 2: Tiến tới Siêu Trí Tuệ (Day 75 - 80)

Sau khi làm chủ các thuật toán Machine Learning cơ bản, mình đã bước sang thế giới của **Large Language Models (LLM)** và kết nối hệ thống với "đám mây".

### 🧠 Cột mốc quan trọng: Ngày 80 - "Mượn não" khổng lồ

Ở ngày này, mình đã thực hiện một bước nhảy vọt: Thay vì chạy các mô hình nhỏ tại máy, mình đã kết nối thành công với **Gemini 2.5 Flash API** của Google.

**Các kỹ thuật đã đạt được:**

* **API Integration:** Kết nối và điều khiển mô hình ngôn ngữ thế hệ mới nhất (2026).
* **Security Best Practices:** * Sử dụng biến môi trường `.env` để bảo vệ API Key.
  * Cấu hình `.gitignore` chuyên nghiệp để ngăn chặn rò rỉ dữ liệu lên GitHub.
* **Environment Management:** Xử lý các xung đột thư viện giữa `google-generativeai`, `protobuf` và `tensorflow` trong môi trường Conda `jarvis_ai`.

### 🛠 Công nghệ mới bổ sung

* **API:** `Google Generative AI SDK` (Gemini 2.5/3.1).
* **Security:** `python-dotenv`.
* **Infrastructure:** gRPC communication protocol.

### 🎥 Demo tính năng hiện tại

* [X] Chat trực tiếp với Gemini 2.5 từ Terminal Python.
* [X] Hệ thống bảo mật "Két sắt" không lộ mã nguồn.
* [ ] *Coming soon (Day 85):* Tích hợp trí nhớ dài hạn (Chat History) vào file JSON.
