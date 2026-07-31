def seo_score(title):
    length = len(title)

    score = 0

    # Ideal length: 50–60 chars
    if 50 <= length <= 60:
        score += 50
    elif 40 <= length < 50 or 60 < length <= 70:
        score += 30
    else:
        score += 10

    # Contains number (good for SEO)
    if any(char.isdigit() for char in title):
        score += 20

    # Contains power words
    power_words = ["best", "top", "guide", "easy", "complete"]
    if any(word in title.lower() for word in power_words):
        score += 30

    return score