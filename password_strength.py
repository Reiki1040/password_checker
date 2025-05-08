import re
import math

# --- [1] 辞書語リストの読み込み ---
def load_common_words():
    try:
        with open("common_words.txt", "r") as f:
            return set(line.strip().lower() for line in f)
    except FileNotFoundError:
        return set()

common_words = load_common_words()

# --- [2] エントロピー推定 ---
def estimate_entropy(password):
    charset = 0
    if re.search(r"[a-z]", password):
        charset += 26
    if re.search(r"[A-Z]", password):
        charset += 26
    if re.search(r"\d", password):
        charset += 10
    if re.search(r"\W", password):
        charset += 32
    if charset == 0:
        return 0.0
    return round(math.log2(charset) * len(password), 2)

# --- [3] 強度評価＋フィードバック付き ---
def check_strength(pw):
    pw_lower = pw.lower()
    feedback = []

    for word in common_words:
        if word in pw_lower:
            feedback.append(f"一般的な単語（例：{word}）は避けましょう")
            break

    if len(pw) < 8:
        feedback.append("文字数が短すぎます（8文字以上推奨）")

    types = 0
    if re.search(r"[a-z]", pw): types += 1
    else: feedback.append("小文字が含まれていません")
    if re.search(r"[A-Z]", pw): types += 1
    else: feedback.append("大文字を含めると強度が上がります")
    if re.search(r"\d", pw): types += 1
    else: feedback.append("数字を追加しましょう")
    if re.search(r"\W", pw): types += 1
    else: feedback.append("記号（例：!@#$）を追加すると安全性が高まります")

    if types <= 2:
        feedback.append("使用している文字種が少ないです（3種類以上推奨）")

    entropy = estimate_entropy(pw)

    if entropy < 30:
        strength = "非常に弱い"
    elif entropy < 40:
        strength = "弱い"
    elif entropy < 60:
        strength = "普通"
    elif entropy < 80:
        strength = "強い"
    else:
        strength = "非常に強い"

    return {
        "strength": strength,
        "entropy": entropy,
        "feedback": feedback
    }
