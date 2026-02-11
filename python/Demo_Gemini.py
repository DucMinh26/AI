import json
import os
from collections import deque
import random

class User:
    def __init__(self, name, age, personality = "friendly"):
        self.name = name
        self.age = age
        self.personality = personality
        self.seen = False
        self.memory = deque(maxlen = 10)
        self.profile = {
            "likes": [],
            "dislikes": [],
            "goals": []

        }
    
    def greet(self):
        if not self.seen:
            self.seen = True
            return f"Xin chào {self.name}! Rất vui được gặp bạn lần đầu tiên."
        else:
            return f"Chào {self.name}! Rất vui được gặp lại bạn."
        
    def remember(self, role, text):
        self.memory.append({
            'role': role,
            'text': text
        })

    def add_like(self, item):
        self.profile['likes'].append(item)
        self.profile['likes'].sort()

    def add_dislike(self, item):
        self.profile['dislikes'].append(item)
        self.profile['dislikes'].sort()
        
    def to_dict(self):
        return{
            "name": self.name,
            "age": self.age,
            "personality": self.personality,
            "seen": self.seen,
            "profile": self.profile,
            "memory": list(self.memory)

        }
    
    def save_to_file(self, file_name = "user_data.json"):
        data = self.to_dict()
        with open(file_name,"w",encoding = "utf-8") as f:
            json.dump(data, f, ensure_ascii= False,indent=4)
            print(f"[System] Đã lưu dữ liệu của {self.name} vào {file_name} ")

    @staticmethod
    def load_user_from_file(file_name = "user_data.json"):
        try:
            with open(file_name,"r", encoding = "utf-8") as f:
                data = json.load(f)
            user = User(data['name'], data['age'],data['personality'])
            user.seen = data['seen']
            user.profile = data['profile']
            memory_data = data.get('memory',[])
            user.memory = deque(memory_data, maxlen=10)

            print(f"[System] Chào mừng {user.name} quay trở lại! ")
            
            return user
        except  (FileNotFoundError, json.JSONDecodeError, ValueError):
            user = User("Khách",1)
            user.save_to_file("user_data.json")
            return user





class Chatbot:
    def __init__(self, bot_name):
        self.bot_name = bot_name

        self.brain_data = {
            "vui": {"Happy": 0.9, "Sad": 0.1},
            "hạnh phúc": {"Happy": 0.95, "Sad": 0.05},
            "buồn": {"Happy": 0.1, "Sad": 0.9},
            "chán": {"Happy": 0.2, "Sad": 0.8},
            "khóc": {"Happy": 0.0, "Sad": 1.0},
            "bình thường": {"Happy": 0.5, "Sad": 0.5}
        }
    
    def binary_search(self, arr, target):
        low = 0
        high = len(arr) - 1
        
        while low <= high:
            mid = (low + high) // 2
            guess = arr[mid]
            if target in guess:
                return guess
            
            if target > guess:
                low = mid + 1
            else:
                high = mid - 1

            return -1
    
    def predict_emotion(self, message):
        msg = message.lower()

        for word, probabilites in self.brain_data.items():
            if word in msg:
                prediction = max(probabilites, key = probabilites.get)
                score = probabilites[prediction]
                return prediction, score
        return "Neutral", 0.5
    
    def smart_greet(self, user):
        normal_greet = [f"Chào {user.name}, mình là {self.bot_name}, hôm nay bạn thế nào!", "Hi there!", f"Mình là {self.bot_name}. Rất vui được gặp lại bạn {user.name}, hôm nay bạn thế nào!"]
        special_greet = [f"Wow mình là {self.bot_name}, hôm nay {user.name} trông tuyệt vời đấy, hôm nay bạn thế nào!", f"{self.bot_name} đây có tin gì hot không người anh em?"]

        if not user.seen:
            user.seen = True
            return f"Xin chào {user.name}! Tôi là trợ lí Ai của bạn, rất vui được gặp bạn lần đầu tiên."
        
        if random.random() < 0.2:
            return random.choice(special_greet)
        return random.choice(normal_greet)
        

    def reply(self, user, message):

        msg_clean = message.strip().lower()
        emotion, score = self.predict_emotion(msg_clean)

        # --- BƯỚC 1: Xử lý cảm xúc (Ưu tiên cao nhất) ---
        if score >= 0.6:
            if emotion == "Happy":
                return f"Nghe giọng bạn vui quá (Độ tin cậy: {score*100:.0f}%)! Có chuyện gì kể mình nghe với?"
            elif emotion == "Sad":
                return f"Nghe giọng bạn buồn quá (Độ tin cậy: {score*100:.0f}%)! Mình có thể giúp gì cho bạn không?"

        # --- BƯỚC 2: Xử lý câu hỏi về sở thích ---
     
        if "thích" in msg_clean and "gì" in msg_clean:
            try:
                keyword = msg_clean.split("thích")[1].split("gì")[0].strip()
            except:
                keyword = ""
            
            if not keyword:
                all_likes = ", ".join(user.profile['likes'])
                
                return f"Bạn thích {all_likes}" if all_likes else "Bạn chưa nói bạn thích gì cả"
            
            # ket_qua = [item for item in user.profile['likes'] if keyword in item]
            ket_qua = self.binary_search(user.profile['likes'], keyword)

            if ket_qua != -1:
                return f"Theo mình biết về {keyword}, thì bạn nói bạn thích {ket_qua}"
            else:
                return f"Mình chưa nghe bạn nhắc gì đến sở thích nào liên quan tới '{keyword}' cả."

        elif "ghét" in msg_clean and "gì" in msg_clean:
            try:
                keyword = msg_clean.split("ghét")[1].split("gì")[0].strip()
            except:
                keyword = ""
            
            if not keyword:
                all_dislikes = ", ".join(user.profile['dislikes'])
                
                return f"Bạn ghét {all_dislikes}" if all_dislikes else "Bạn chưa nói bạn ghét gì cả"
            
            # ket_qua = [item for item in user.profile['likes'] if keyword in item]
            ket_qua = self.binary_search(user.profile['dislikes'], keyword)

            if ket_qua != -1:
                return f"Theo mình biết về {keyword}, thì bạn nói bạn ghét {ket_qua}"
            else:
                return f"Mình chưa nghe bạn nhắc gì liên quan tới '{keyword}' cả."

        elif "thích" in msg_clean and "gì" not in msg_clean and "không" not in msg_clean:
            item = msg_clean.split("thích",1)[1].strip()
            user.add_like(item)

            if user.personality == "friendly":
                return f"Tôi đã nhớ bạn thích {item} rồi nhé"
            else:
                return f"Hừ ai thèm nhớ bạn thích {item} chứ"
            
        elif "ghét" in msg_clean and "gì" not in msg_clean and "không" not in msg_clean:
            item = msg_clean.split("ghét",1)[1].strip()
            user.add_dislike(item)

            if user.personality == "friendly":
                return f"Tôi đã nhớ bạn ghét {item} rồi nhé"
            else:
                return f"Hừ ai thèm nhớ bạn ghét {item} chứ"
        
        elif "tên" in msg_clean:
            return f"Tên bạn là {user.name}"
        
        elif "tuổi" in msg_clean:
            return f"Bạn {user.age} tuổi"
        
        else:
            return "Tôi đang lắng nghe đây"

class Admin(User):
    def __init__(self, name, age):
        super().__init__(name, age, personality = "serious")
        self.role = "Admin"

    def greet(self):
        return f"Xin chào ADMIN {self.name}"
    
    def reset_system(self):
        print("[ADMIN ALERT] Đang tiến hành xóa toàn bộ dữ liệu hệ thống ... ")

        try:
            if os.path.exists("user_data.json"):
                os.remove("user_data.json")
                return f"Đã xóa sạch dữ liệu của user trên bộ nhớ và hệ thống"

            else:
                return "Không có dữ liệu để xóa"
            
        except Exception as e:
            return f"Lỗi khi xóa: {e}"

    def save_to_file(self, file_name="user_data.json"):
        print(f"[System] Đã đăng xuất")

bot = Chatbot("Jarvis")
current_user = None

print("---------------------------- Hệ thống đăng nhập ----------------------------")
ten_dang_nhap = input("Vui lòng nhập tên đăng nhập: ")

if ten_dang_nhap == "admin":
    current_user = Admin("Adminitrator", 99)

else:
    current_user = User.load_user_from_file()
    if current_user.name != ten_dang_nhap:
        current_user.name = ten_dang_nhap

if current_user is None:
    current_user = User("Khách", 1)

print(f"\n--- Bắt đầu chat với {current_user.name} (chat 'exit' để thoát) ---")    
print(f"Bot: {bot.smart_greet(current_user)} ")

while True:
    try:
        
        user_input = input(f"{current_user.name}: ")

        if user_input.strip().lower() == "exit":
                current_user.save_to_file()
                print("Bot: Tạm biệt!!")    
                break
            
        if hasattr(current_user, "reset_system") and user_input == "reset":
            kq = current_user.reset_system()
            print(f"BOT: {kq}")
            continue

        rep = bot.reply(current_user,user_input)
        print(f"Bot: {rep}")
        

        current_user.remember(current_user.name, user_input)
        current_user.remember(bot.bot_name, rep)

    except KeyboardInterrupt:
        current_user.save_to_file()
        print("\nĐã dừng chương trình và lưu dữ liệu")
        break

