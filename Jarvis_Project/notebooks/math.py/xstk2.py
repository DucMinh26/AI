import random

brain_data = {
    "vui": {"Happy": 0.9, "Sad": 0.1},
    "buồn": {"Happy": 0.1, "Sad": 0.9},
    "bình thường": {"Happy": 0.5, "Sad": 0.5}
}

def bot_reply():
    normal_greet = ["Chào bạn!", "Hi there!", "Rất vui được gặp bạn."]
    specical_greet = ["Hôm nay bạn trông tuyệt vời đấy!", "Có gì mới không người bạn?"]

    if random.random() < 0.2:
        return random.choice(specical_greet)
    
    return random.choice(normal_greet)
    
def predict_emotion(mess):
    msg = mess.lower()

    for word, probabilites in brain_data.items():
        if word in msg:
            prediction = max(probabilites, key = probabilites.get)
            score = probabilites[prediction]
            return prediction, score
        
    return "Neutral", 0.5

msg = "Hôm nay mình thấy rất vui"
emotion, confidence = predict_emotion(msg)
print(f"Bot đoán bạn đang: {emotion} (Độ tin cậy: {confidence*100}%)")
        