# =========================================
# AUTOMATED META TITLE GENERATOR (AI PROJECT)
# Student: Esha Fatima
# Institute: RPI
# Trainer: Sir Mehmood Ali
# =========================================

import streamlit as st
from model import extract_keywords

# -------------------------------
# Improved Title Generator
# -------------------------------
def generate_titles(keywords):
    if not keywords:
        return ["Best Guide for Your Topic"]

    # Combine all keywords into one phrase
    base = " ".join(keywords).title()

    titles = [
        f"{base} for Beginners – Step-by-Step Guide 2026",
        f"Learn {base} Fast – Complete Tutorial (2026)",
        f"{base} Explained Simply – Beginner Friendly Guide",
        f"Master {base} in 2026 (Easy Step-by-Step Method)",
        f"{base} Tutorial – Everything You Need to Know"
    ]

    return titles

# -------------------------------
# Improved SEO Scoring Function
# -------------------------------
def seo_score(title):
    score = 0
    t = title.lower()

    # Keyword presence (basic assumption)
    if len(t.split()) >= 3:
        score += 20

    # Intent keywords
    if "beginner" in t or "guide" in t:
        score += 20

    # Tutorial / step
    if "step" in t or "tutorial" in t:
        score += 20

    # Year factor
    if "2026" in t:
        score += 10

    # Length optimization
    if 50 <= len(title) <= 70:
        score += 20

    # Power words
    if any(word in t for word in ["best", "easy", "fast", "complete", "master"]):
        score += 10

    return min(score, 100)

# -------------------------------
# UI Design
# -------------------------------
st.set_page_config(page_title="Meta Title Generator", layout="centered")

st.title("🚀 AI Meta Title Generator")
st.write("Generate SEO-optimized titles using AI + NLP")

user_input = st.text_area("Enter your content or keywords:")

if st.button("Generate Titles"):
    if user_input.strip() == "":
        st.warning("Please enter some text!")
    else:
        keywords = extract_keywords(user_input)
        titles = generate_titles(keywords)

        st.subheader("🔑 Extracted Keywords")
        st.write(keywords)

        st.subheader("✨ Generated Titles")

        for t in titles:
            score = seo_score(t)

            st.write(f"👉 {t}")
            st.progress(score / 100)
            st.write(f"SEO Score: {score}/100")
            st.markdown("---")
