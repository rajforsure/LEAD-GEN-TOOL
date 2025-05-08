# lead_score.py

def score_lead(lead_text):
    score = 0
    text = lead_text.lower()  # make case-insensitive

    if "ceo" in text or "founder" in text:
        score += 30
    if "marketing" in text:
        score += 20
    if "startup" in text:
        score += 10
    if "einstein" in text:
        score += 15  # just for fun on test site

    return score

if __name__ == "__main__":
    print(score_lead("Albert Einstein"))
