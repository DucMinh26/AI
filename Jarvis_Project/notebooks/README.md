<h1 style ="color='red'">QUY TRÌNH CÁC BƯỚC TẠO RA  AI</h1>

## Bước 1: Xác định bài toán & Thu thập dữ liệu (Define & Collect)

Trước khi code, bạn phải biết mình định làm gì.

* **Xác định:** Đây là bài toán Phân loại (Chó hay Mèo?) hay Dự báo (Giá nhà bao nhiêu?).
* **Thu thập:** Lấy dữ liệu từ file CSV, Excel, SQL, hoặc các kho dữ liệu khổng lồ trên mạng.
* **Thành phần:** Dữ liệu đầu vào ( **Features** ) và đáp án đúng ( **Labels/Targets** ).

---

## Bước 2: Tiền xử lý dữ liệu (Data Preprocessing)

Đây là lúc bạn làm sạch "nguyên liệu thô".

* **Dọn dẹp:** Xử lý các ô bị trống (Null), xóa bỏ các dữ liệu rác hoặc bị trùng.
* **Chuẩn hóa (Normalization/Scaling):** Đưa các con số về cùng một hệ quy chiếu (ví dụ từ **$0$** đến **$1$**) để AI không bị "choáng" bởi các số quá lớn.
* **Chia dữ liệu:** Chia làm 2 phần:
  * **Train set (80%):** Cho AI học.
  * **Test set (20%):** Để dành đi thi, tuyệt đối không cho AI xem trước.

---

## Bước 3: Xây dựng cấu trúc mô hình (Model Architecture)

Thiết kế "mạch nơ-ron" cho bộ não.

* **Chọn loại mô hình:** CNN (cho ảnh), RNN/Transformer (cho văn bản), hoặc Linear Regression (cho con số đơn giản).
* **Thiết lập lớp (Layers):** Quyết định xem bộ não này cần bao nhiêu tầng, mỗi tầng có bao nhiêu nơ-ron (như cái `Dense(64)` mà bạn hỏi đấy).

---

## Bước 4: Biên dịch & Thiết lập (Compile)

Cài đặt "hệ điều hành" cho việc học.

* **Loss Function:** Chọn thước đo để biết AI đang sai bao nhiêu.
* **Optimizer:** Chọn "người thầy" chỉ đường để AI sửa sai (như Adam).
* **Metrics:** Chọn cái để con người nhìn vào đánh giá (như Accuracy).

---

## Bước 5: Huấn luyện (Training / Fitting)

Đây là giai đoạn "đèn sách".

* **Lệnh thần thánh:** `model.fit()`.
* **Quá trình:** AI thực hiện hàng ngàn lần vòng lặp:  **Dự đoán **$\rightarrow$** So sánh đáp án **$\rightarrow$** Thấy sai **$\rightarrow$** Sửa nơ-ron **$\rightarrow$** Dự đoán lại** .
* **Epochs:** Số lần AI đọc đi đọc lại toàn bộ đống sách giáo khoa.

---

## Bước 6: Đánh giá & Triển khai (Evaluation & Deployment)

Kiểm tra xem AI có "thông minh thật" hay chỉ "học vẹt".

* **Kiểm tra:** Dùng tập **Test set** ở Bước 2 để chấm điểm.
* **Tinh chỉnh (Tuning):** Nếu điểm thấp, quay lại Bước 3 để thêm nơ-ron hoặc Bước 2 để dọn dữ liệu sạch hơn.
* **Triển khai:** Lưu mô hình lại và gắn nó vào ứng dụng, web hoặc robot để nó bắt đầu làm việc ngoài đời thực.
