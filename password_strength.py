import re

def check_strength(pw):
    if len(pw) < 6:
        return "弱い（6文字未満）"
    
    score = 0
    if re.search(r"[a-z]", pw):
        score += 1
    if re.search(r"[A-Z]", pw):
        score += 1
    if re.search(r"\d", pw):
        score += 1
    if re.search(r"\W", pw):  # 記号（英数字以外）
        score += 1

    if score <= 1:
        return "弱い"
    elif score == 2:
        return "普通"
    elif score == 3:
        return "強い"
    else:
        return "非常に強い"
