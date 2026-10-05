import os
from pathlib import Path
import streamlit as st

from services.recommender import recommend_projects
from services.pdf_utils import extract_pdf_text, chunk_text
from services.ai_client import ask_gemini, ask_ollama

BASE = Path(__file__).parent

st.set_page_config(page_title="AI Project Guide", page_icon="🤖", layout="wide")

st.title("🤖 AI Project Guide")
st.caption("Find suitable AI/Data Science projects, upload project documents, and get an AI-assisted project plan.")

with st.sidebar:
    st.header("Project Finder")
    skill = st.selectbox("Your main skill", ["Python", "Java", "SQL", "Machine Learning", "NLP", "Data Science", "Web Development"])
    level = st.selectbox("Level", ["Beginner", "Intermediate", "Advanced"])
    domain = st.selectbox("Preferred domain", ["Any", "Education", "Healthcare", "Finance", "Career", "Environment", "Business"])
    recommend = st.button("Recommend Projects", use_container_width=True)

if "recommendations" not in st.session_state:
    st.session_state.recommendations = []

if recommend:
    st.session_state.recommendations = recommend_projects(skill, level, domain)

if st.session_state.recommendations:
    st.subheader("Recommended Projects")
    for i, p in enumerate(st.session_state.recommendations, 1):
        with st.container(border=True):
            st.markdown(f"### {i}. {p['title']}")
            st.write(p['description'])
            st.write(f"**Technologies:** {p['technologies']}")
            st.write(f"**Difficulty:** {p['difficulty']}  |  **Domain:** {p['domain']}")
            st.write(f"**Why it fits:** {p['reason']}")

st.divider()

left, right = st.columns(2)
with left:
    st.subheader("📄 Project Document Analyzer")
    uploaded = st.file_uploader("Upload a PDF project document", type=["pdf"])
    if uploaded:
        text = extract_pdf_text(uploaded)
        st.success(f"PDF loaded successfully — {len(text):,} characters extracted.")
        chunks = chunk_text(text)
        st.info(f"Created {len(chunks)} searchable text chunks.")
        with st.expander("Preview extracted text"):
            st.text(text[:4000] if text else "No readable text was found in this PDF.")

with right:
    st.subheader("💡 Project Guide")
    project_name = st.text_input("Enter a project name", placeholder="AI-Based Interview Assessment System")
    if project_name:
        st.markdown(f"**Suggested development flow for {project_name}:**")
        for step in [
            "1. Define the problem and users.",
            "2. Collect and prepare the required data.",
            "3. Build the core Python/ML logic.",
            "4. Create the Streamlit user interface.",
            "5. Test with sample inputs and handle errors.",
            "6. Document the architecture, results, and future scope.",
        ]:
            st.write(step)

st.divider()
st.subheader("💬 AI Assistant")
st.caption("Gemini and Ollama are optional. The app still runs without either service configured.")
question = st.text_area("Ask about your project", placeholder="How should I build an AI resume analyzer?")
provider = st.selectbox("AI provider", ["Built-in Guide", "Gemini", "Ollama"])

if st.button("Get Answer"):
    if not question.strip():
        st.warning("Please enter a question.")
    elif provider == "Gemini":
        answer = ask_gemini(question)
        st.markdown(answer)
    elif provider == "Ollama":
        answer = ask_ollama(question)
        st.markdown(answer)
    else:
        st.markdown(
            "**Recommended approach:** Start with the problem statement, define inputs and outputs, "
            "choose the simplest suitable model, build a small working version, test it, and then add advanced features."
        )

st.divider()
st.caption("AI Project Guide • Python 3.11 • Streamlit")
