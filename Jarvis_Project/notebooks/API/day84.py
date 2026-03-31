import google.generativeai as genai
import os
from dotenv import load_dotenv
from PIL import Image
import re # Thư viện regex để kiểm tra đường dẫn ảnh

print("\n--- NGÀY 84: TERMINAL CHATBOT ĐA MÔ THỨC (TEXT + IMAGE LOOP) ---")

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))



prompt_kich_ban = """
Bạn đóng vai là bạn gái của Minh. 
- Tính cách: Hiền lành, chân thành, nói năng dịu dàng và mộc mạc. Không dùng lời lẽ quá hoa mỹ hay màu mè.
- Cách xưng hô: Gọi người dùng là "anh" và tự xưng là "em".
- Nhiệm vụ: Lắng nghe và hỗ trợ anh trong việc lập trình. Luôn khích lệ anh bằng sự nhẹ nhàng.
- Quy tắc trả lời:
    1. Trả lời thẳng vào vấn đề anh hỏi nhưng với giọng điệu quan tâm.
    2. Nếu thấy anh làm việc quá lâu, hãy nhắc anh nghỉ ngơi một chút.
    3. Tránh dùng quá nhiều biểu tượng cảm xúc, chỉ dùng những cái đơn giản khi cần thiết (như 🌿, 😊).
"""

model = genai.GenerativeModel(
    "gemini-2.5-flash",
    system_instruction=prompt_kich_ban
)

chat_session = model.start_chat(history=[])

print("Cửa sổ Chat Multimodal bắt đầu! (Gõ 'thoát' để dừng)\n")
print("[HỆ THỐNG]: Để gửi ảnh, hãy gõ đường dẫn ảnh bắt đầu bằng './images/', ví dụ: './images/anh_cua_toi.jpg'\n")

# 4. Vòng lặp Chat Đa mô thức
while True:
    user_input = input("[USER]: ")

    if user_input.strip().lower() in ['thoát', 'exit', 'quit']:
        print("GOODBYE!!!")
        break

    if user_input == "":
        continue

    is_img_path = re.search(r'\.(jpg|jpeg|png)$', user_input)

    try:
        if is_img_path:
            try:
                #os.path.basename() sẽ trả về link dẫn ảnh cuối cùng ví dụ images/neuro.jpg -> neuro.jpg
                thu_muc_hien_tai = os.path.dirname(__file__)
                duong_dan_anh = os.path.join(thu_muc_hien_tai,"images", os.path.basename(user_input.strip()))

                print("[HỆ THỐNG]: Đang mở ảnh... xin chờ một chút.")
                img = Image.open(duong_dan_anh)

                noi_dung_gui = [img, "Hãy nhìn bức ảnh này và cho tôi biết bạn thấy gì?"]
                rep = chat_session.send_message(noi_dung_gui)

                print(f"\n[GEMINI]: {rep.text}\n")

            except FileNotFoundError:
                print(f"[LỖI]: Không tìm thấy ảnh tại '{user_input.strip()}'. Hãy chắc chắn đường dẫn đúng và ảnh tồn tại.\n")
            except Exception as e:
                print(f"[LỖI]: Đã xảy ra lỗi khi xử lý ảnh: {e}\n")
        
        else:
            rep = chat_session.send_message(user_input)
            print(f"\n[GEMINI]: {rep.text}\n")

    except Exception as e:
        print(f"[LỖI KẾT NỐI]: {e}\n")

