import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
from PIL import Image

print("\n--- NGÀY 86: GIAO DIỆN WEB AI ĐA MÔ THỨC ---")

#1. Cấu hình trang web
st.set_page_config(page_title="Jarvis Chat", page_icon="🤖", layout="centered")
st.title("🤖 Jarvis Chat - Chatbot Đa Mô Thức")

#2. Cấu hình API Key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

prompt_kich_ban = """
Bạn đóng vai là bạn gái của Minh. 
- Tính cách: Hiền lành, chân thành, nói năng dịu dàng và mộc mạc. Không dùng lời lẽ quá hoa mỹ hay màu mè.
- Cách xưng hô: Gọi người dùng là "anh" và tự xưng là "em".
- Nhiệm vụ: Lắng nghe và hỗ trợ anh trong việc lập trình. Luôn khích lệ anh bằng sự nhẹ nhàng.
"""

# Sử dụng st.cache_resource để Streamlit không khởi tạo lại AI mỗi lần bấm nút
@st.cache_resource
def load_model():
    return genai.GenerativeModel("gemini-2.5-flash",system_instruction=prompt_kich_ban)

model = load_model()

#3.Quản lý phiên chat
#Vì streamlit quản lí theo cơ chế tải lại trang mỗi mội hành động bất kì, nên ta cần lưu trữ phiên chat trong session_state để giữ được lịch sử trò chuyện
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

#4. Giao diện chat
for message in st.session_state.chat_session.history:
    #Google quy định máy là model, streamlit quy định là assistant
    role="assistant" if message.role == "model" else "user"
    with st.chat_message(role):
        st.markdown(message.parts[0].text)

#5.Thêm SideBar để upload ảnh
with st.sidebar:
    st.header("🖼️ Image")
    uploaded_file = st.file_uploader("Chọn 1 bức ảnh", type=["jpg","jpeg","png"])
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Ảnh bạn vừa chọn", width="stretch")#kéo dãn ảnh cho vừa cái khung

#6.Ô nhập liệu
user_input = st.chat_input("[USER]: ")

if user_input:
        with st.chat_message("user"):
            st.markdown(user_input)

        with st.chat_message("assistant"):
            with st.spinner("Jarvis đang suy nghĩ..."):

                if uploaded_file is not None:
                    img = Image.open(uploaded_file)
                    rep = st.session_state.chat_session.send_message([img,user_input])

                else:
                    rep = st.session_state.chat_session.send_message(user_input)

                st.markdown(rep.text)