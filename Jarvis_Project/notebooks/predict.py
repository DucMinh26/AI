import joblib
import os
import pandas as pd

current_dir = os.path.dirname(__file__)

model_path = os.path.join(current_dir, "model_du_doan_mua_xe.pkl")

try:
    load_model = joblib.load(model_path)
    print("--- TRIỆU HỒI BỘ NÃO AI THÀNH CÔNG ---")

    kh_moi = pd.DataFrame([[30, 15000]], columns=['Tuổi', 'Lương ($)'])
    kq = load_model.predict(kh_moi)
    print(f"Kết quả dự đoán: {'Mua xe' if kq[0] == 1 else 'Không mua xe'}")

except FileNotFoundError:
    print(f"Không tìm thấy file mô hình tại {model_path}. Vui lòng đảm bảo rằng file model_du_doan_mua_xe.pkl đã tồn tại.")
