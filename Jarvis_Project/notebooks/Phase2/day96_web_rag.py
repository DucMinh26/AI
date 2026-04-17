import streamlit as st
import os
from operator import itemgetter
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables import RunnablePassthrough
import tempfile
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

print("\n--- NGÀY 96: HỢP NHẤT RAG VÀO STREAMLIT ---")

#1. Cấu hình trang web
st.set_page_config(page_title="Jarvis - trợ lí đọc tài liệu", layout="centered")
st.title("Jarvis - trợ lí đọc tài liệu")

#2. Khởi tạo bộ não RAG
@st.cache_resource
def khoi_tao_rag():
    load_dotenv()

    llm=ChatGroq(
        model="llama-3.3-70b-versatile",
        api_key=os.getenv("GROQ_API_KEY"),
        temperature=0.2
    )

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    vector_db=Chroma(persist_directory="F:/Neuro-sama/Jarvis_Project/notebooks/Phase2/database_groq", embedding_function=embeddings)

    nguoi_tim_kiem = vector_db.as_retriever(search_kwargs={"k":3})

    mau_lenh = """
    Bạn là Jarvis, một trợ lý AI thông minh chuyên phân tích tài liệu.
    Hãy trả lời câu hỏi dựa TRÊN TÀI LIỆU được cung cấp dưới đây.
    Nếu tài liệu không có thông tin, hãy thẳng thắn trả lời "Tôi không tìm thấy thông tin này trong tài liệu", không được tự bịa ra.
    
    ĐIỀU KIỆN BẮT BUỘC: Ở cuối câu trả lời, bạn LUÔN LUÔN phải trích dẫn (Tên file và Số trang) mà bạn đã dùng để lấy thông tin.
    
    TÀI LIỆU CỦA NGƯỜI DÙNG:
    {context}
    """

    prompt = ChatPromptTemplate.from_messages([
        ('system', mau_lenh),
        MessagesPlaceholder(variable_name='history'),
        ('human', '{input}')
    ])

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs) if docs else "Không có tài liệu nào được tìm thấy."
    
    day_chuyen_rag = (
        {
            "context": itemgetter("input") | nguoi_tim_kiem | format_docs,
            "input": itemgetter("input"),
            "history": itemgetter("history")
        }
        |prompt
        |llm
        |StrOutputParser()
    )

    return day_chuyen_rag

day_chuyen_rag = khoi_tao_rag()

if 'store' not in st.session_state:
    st.session_state.store = {}

def get_session_history(session_id: str):
    if session_id not in st.session_state.store:
        st.session_state.store[session_id] = ChatMessageHistory()
    return st.session_state.store[session_id]

day_chuyen_rag_with_memory = RunnableWithMessageHistory(
    day_chuyen_rag,
    get_session_history,
    input_messages_key='input',
    history_messages_key='history'
)

session_id = "phien chat web"

if session_id in st.session_state.store:
    for msg in st.session_state.store[session_id].messages:
        role='user' if msg.type =='human' else 'assistant'
        with st.chat_message(role):
            st.markdown(msg.content)

with st.sidebar:
    st.header("SETTING")
    if st.button("XÓA LỊCH SỬ CHAT"):
        st.session_state.store[session_id] = ChatMessageHistory()
        st.rerun()

    st.divider()

    st.header("NHẬP TÀI LIỆU")
    up_file = st.file_uploader("Tải lên file PDF của bạn", type=["pdf"])

    if st.button("XỬ LÝ TÀI LIỆU"):
        if up_file is not None:
            with st.spinner("Đang băm nhỏ và nhúng tài liệu..."):
                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
                    tmp_file.write(up_file.getvalue())
                    tmp_file_path = tmp_file.name

                try:
                    loader = PyPDFLoader(tmp_file_path)
                    docs = loader.load()

                    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
                    chunks = text_splitter.split_documents(docs)

                    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
                    vecter_db = Chroma(persist_directory="F:/Neuro-sama/Jarvis_Project/notebooks/Phase2/database_groq", embedding_function=embeddings)

                    vecter_db.add_documents(chunks)

                    st.success(f"Đã nạp xong {len(chunks)} đoạn dữ liệu từ file!")
                    
                except Exception as e:
                    st.error(f"Có lỗi xảy ra: {e}")
                finally:
                    # Dọn dẹp file tạm
                    os.remove(tmp_file_path)
        else:
            st.warning("Bạn chưa chọn file PDF nào!")

user_input = st.chat_input("Nhập câu hỏi của bạn về tài liệu...")

if user_input:
    with st.chat_message('user'):
        st.markdown(user_input)

    with st.chat_message("assistant"): 
        with st.spinner("Jarvis đang suy nghĩ..."):
            ket_qua = day_chuyen_rag_with_memory.invoke(
                    {"input": user_input},
                    config={"configurable": {"session_id": session_id}}
                )
            st.markdown(ket_qua)