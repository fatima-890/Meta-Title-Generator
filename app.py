# =========================================
# AUTOMATED META TITLE GENERATOR (AI PROJECT)
# Student: Esha Fatima
# Institute: RPI
# Trainer: Sir Mehmood Ali
# =========================================

import streamlit as st
from model import extract_keywords
from seo import seo_score

def generate_titles(keywords):
    if not keywords:
        return ["Best Guide for Your Topic"]

    base = keywords[0].title()

    titles = [
        f"Best {base} Guide in 2026",
        f"Top 10 {base} Tips You Must Know",
        f"{base} Secrets for Beginners",
        f"Complete {base} Tutorial",
        f"How to Master {base} Easily"
    ]

    return titles

# UI
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

        st.subheader("🔑 Keywords")
        st.write(keywords)

        st.subheader("✨ Generated Titles")

        for t in titles:
            score = seo_score(t)
            st.write(f"👉 {t}")
            st.progress(score / 100)
            st.write(f"SEO Score: {score}/100")
            st.write("---")