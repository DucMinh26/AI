tu_Dien_teencode = {
    "ko": "không",
    "dc": "được",
    "hn": "hà nội",
    "bt": "biết",
    "nyc": "người yêu cũ",
    "o": "ở",
    "hom": "hôm",
    "luon": "luôn"
}

def dich_tin_nhan(text):
    cac_tu = text.split()

    kq = []

    for tu in cac_tu:
        tu_lower = tu.lower()

        if tu_lower in tu_Dien_teencode:
            nghia_day_du = tu_Dien_teencode[tu_lower]
            kq.append(nghia_day_du)

        else:
            kq.append(tu_lower)

    return " ".join(kq)

msg = "hom qua gap nyc o hn ko bt sao luon"
print(f"Gốc:{msg} ")
print(f"Dịch:{dich_tin_nhan(msg)} ")

