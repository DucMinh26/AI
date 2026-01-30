import json
import random

PERSONALITY = {
    "friendly": {
        "greet_first": [
            "Hi {name}, rất vui được gặp bạn!",
            "Chào {name}! Mình là AI đây 😊",
        ],
        "greet_again": [
            "Lại gặp bạn rồi {name}!",
            "Chúng ta gặp lại nhau rồi nè {name}",
        ],
        "under_18": [
            "Chào em {name}, hôm nay thế nào?",
        ]
    },
    "tsundere": {
        "greet_first": [
            "Ồ, bạn là {name} hả? Đừng nghĩ mình quan tâm đâu nhé!",
            "Chào... {name}. Mình không có gì đặc biệt đâu.",
        ],
        "greet_again": [
            "Lại là bạn à, {name}? Đừng có làm phiền mình nữa đấy!",
            "Ồ, lại gặp bạn rồi... {name}. Mình không vui đâu nhé.",
        ],
        "under_18": [
            "Chào em... {name}. Đừng có nghĩ mình sẽ chiều chuộng em đâu.",
        ]
    }
}



def create_user ():
    while True:
        name = input("Enter your name: ").strip()
        if not name:
            print("Name cannot be empty")
            continue
        break
    
    p = input(f"Choose personality (friendly/tsundere): ").strip().lower()
    p = "friendly" if p not in PERSONALITY else p

    while True:
        try:
            age = int(input("Enter your age: "))
            break
        except ValueError:
            print("Age must be a number")


    return {"name":name, "age":age, "personality":p, "seen":False, "memory": []}

def show_users(users):
    if not users:
        print("No users yet")
        return

    for idx, i in enumerate(users, 1):
        print(f"{idx}.Name: {i['name']}, Age: {i['age']}, Personality: {i['personality']}, Seen: {i['seen']}")

def load_users():
    try:
        with open("users.json","r",encoding="utf-8") as f:
            users = json.load(f)

            for user in users:
                user.setdefault("seen", False)
                user.setdefault("memory", [])
                user.setdefault("personality", "friendly")
            return users
        
    except FileNotFoundError:
        return []
    
def save_users(users):
    with open("users.json","w",encoding="utf-8") as f:
        json.dump(users,f,ensure_ascii=False, indent=4)

def find_user(users,name):
    for user in users:
        if user['name'].lower() == name.lower():
            return user
    return None

def update_user(users):
    name = input("Enter name you want to update: ")
    user = find_user(users,name)

    if not user:
        print("User not found")
        return
    
    while True:
        try:
            new_name = input("Enter new name: ")
            new_age = int(input("Enter new age: "))
            new_seen =input("Enter new seen (True/False): ").strip().lower()
            new_personality = input("Enter new personality (friendly/tsundere): ").strip().lower()
            new_personality = "friendly" if new_personality not in PERSONALITY else new_personality
            break
        except ValueError:
            print("Age must be a number")
    user['name'] = new_name
    user['age'] = new_age
    user['seen'] = new_seen == 'true'
    user['personality'] = new_personality
    save_users(users)
    print("User updated successfully")

def delete_user(users):
    name = input("Enter name you want to delete: ")
    
    new_users = [user for user in users if user['name'].lower() != name.lower()]
    
    if len(new_users) < len(users):
        save_users(new_users)
        print("User deleted successfully")
        return new_users
    else:
        print("User not found")
        return users

def respond(user):
    p = PERSONALITY[user['personality']]

    if not user['seen']:
        user['seen'] = True
        return choose(p['greet_first'],user)

    if user['age'] <18:
        return choose(p['under_18'],user)

    return choose(p['greet_again'],user)

def respond_chat(user,message):
    remember(user, "user", message)

    memory = user['memory']

    if "tên" in message.strip().lower():
        reply = f"Tên bạn là {user['name']}"
    
    elif "tuổi" in message.strip().lower():
        reply = f"Bạn {user['age']} tuổi rồi"

    elif len(memory) >= 4:
        last_user_msg = memory[-2]['text']
        reply = f"Như mình đã nói trước đó, {last_user_msg}"

    else:
        reply = respond(user)

    remember(user, "AI", reply)
    return reply

def choose(lines,user):
    return random.choice(lines).format(**user)

def remember(user, role, text):
    MAX_MEMORY = 10

    user['memory'].append({
        "role": role,
        "text": text
    })

    if len(user['memory']) > MAX_MEMORY:
        user['memory'] = user['memory'][-MAX_MEMORY:]




users = load_users()

while True:
    cmd = input("enter add,show,update,delete,chat,exit: ").strip().lower()

    if cmd =="add":
        users.append(create_user())
        save_users(users)
        print("Save!")

    elif cmd =="show":
        show_users(users)
        

    elif cmd =="exit":
        print("Goodbye!")
        break
    
    elif cmd =="update":
        update_user(users)

    elif cmd =="delete":
        users =delete_user(users)
        
    elif cmd =="chat":
        name = input("Enter your name: ").strip()
        user = find_user(users,name)
        
        if not user:
            print("I don't know you yet")
            continue
        
        print(f"Chat mode (type 'bye' to leave)")

        while True:
            msg = input("You: ").strip()

            if msg.lower() == 'bye':
                print("AI: BYE!")
                break

            reply = respond_chat(user, msg)
            print(f"AI: {reply}")  
            save_users(users)

    else:
        print("Try add,show,update,delete,chat,exit: ")