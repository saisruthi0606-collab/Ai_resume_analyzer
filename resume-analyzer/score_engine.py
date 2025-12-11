import re

def clean_text(text):
    return re.sub(r'[^a-zA-Z0-9 ]', ' ', text.lower())

def calculate_resume_score(resume_text, jd_text):
    resume = clean_text(resume_text)
    jd = clean_text(jd_text)

    jd_keywords = jd.split()
    found = []
    score = 0

    for word in jd_keywords:
        if word in resume:
            found.append(word)
            score += 2

    score = min(score, 100)
    return score, found
