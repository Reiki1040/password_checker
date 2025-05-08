import re

def check_strength(pw):
    length = len(pw)
    
    if length < 8:
        return "弱い（8文字未満）"

    score = 0
    types = 0

    if re.search(r"[a-z]", pw):
        score += 1
        types += 1
    if re.search(r"[A-Z]", pw):
        score += 1
        types += 1
    if re.search(r"\d", pw):
        score += 1
        types += 1
    if re.search(r"\W", pw):  # 記号
        score += 1
        types += 1

    if types <= 2:
        return "弱い（種類が少なすぎる）"

    if length >= 12:
        score += 1  # 長さボーナス

    # 最終判定（スコア範囲：0〜5）
    if score <= 2:
        return "弱い"
    elif score == 3:
        return "普通"
    elif score == 4:
        return "強い"
    else:
        return "非常に強い"
