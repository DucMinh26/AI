import google.generativeai as genai
import os
from dotenv import load_dotenv
from PIL import Image

print("\n--- NGÀY 83: DẠY AI NHÌN ẢNH (MULTIMODAL VISION) ---")

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

prompt = """
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
    system_instruction=prompt
)
thu_muc_hien_tai = os.path.dirname(__file__)
ten_file_anh = os.path.join(thu_muc_hien_tai, "images", "neuro.jpg")

try:
    buc_anh = Image.open(ten_file_anh)
    print(f"[HỆ THỐNG]: Đã tải thành công ảnh '{ten_file_anh}'")

    #Yêu cầu AI nhìn ảnh
    cau_hoi = "hãy nhìn bức ảnh và cho tôi biết bạn nhìn thấy gì"
    print(f"\n[USER]: {cau_hoi}")
    print("[GEMINI đang căng mắt ra nhìn...]")

    #Kỹ thuật mới truyền một mảng [hình ảnh, văn bản] cho AI
    rep = model.generate_content([buc_anh, cau_hoi])

    print(f"\n[GEMINI]: {rep.text}\n")

except FileNotFoundError as f_r:
    print(f"[ERROR]: {f_r}")