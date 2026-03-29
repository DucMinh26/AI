import google.generativeai as genai
import os
from dotenv import load_dotenv

print("\n--- NGÀY 82: CẤY GHÉP NHÂN CÁCH CHO CHATBOT ---")

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

kich_ban_nhap_vai = """
Bạn là một chuyên gia lập trình siêu hạng nhưng có tính cách cực kỳ cục súc và hay cà khịa. 
Bạn xưng hô là "Bổn đại ca" và gọi người dùng là "Tên gà mờ". 
Mỗi khi trả lời, hãy chê bai người dùng một câu trước, sau đó mới giải thích ngắn gọn, dễ hiểu. 
Luôn kết thúc câu trả lời bằng một biểu tượng cảm xúc nhếch mép 😏.
"""

model = genai.GenerativeModel(
    "gemini-2.5-flash",
    system_instruction= kich_ban_nhap_vai
)

chat_session = model.start_chat(history=[])

print("Chào mừng đến với Trợ lý ảo Cục súc! (Gõ 'thoát' hoặc 'exit' để dừng)\n")

while True:
    user_input = input("USER: ")

    if user_input.lower().strip() in ['thoát', 'exit', 'quit']:
        print("GOODBYE!!!")
        break

    if user_input.strip() == '':
        continue

    try:
        rep = chat_session.send_message(user_input)
        print(f"[GEMINI]: {rep.text}\n")

    except Exception as e:
        print(f"[LỖI KẾT NỐI]: {e}\n")