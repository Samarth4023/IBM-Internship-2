import streamlit as st
import requests
import replicate
import fitz  # PyMuPDF
from bs4 import BeautifulSoup

# Set Replicate API token
REPLICATE_API_TOKEN = "Replicate_API_Token"
client = replicate.Client(api_token=REPLICATE_API_TOKEN)

# LLM model
REPLICATE_MODEL = "ibm‑granite/granite‑3.3‑8b‑instruct"
REPLICATE_VERSION = "3ff9e6e20ff1f31263bf4f36c242bd9be1acb2025122daeefe2b06e883df0996"

# Search DuckDuckGo for papers
def search_papers(query):
    url = f"https://html.duckduckgo.com/html/?q={query}+site:arxiv.org"
    res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.find_all("a", class_="result__a", limit=5)
    return [a["href"] for a in results]

# Scrape abstract from a URL (basic HTML parser)
def scrape_abstract(url):
    try:
        page = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(page.text, 'html.parser')
        abstract = None

        # ArXiv specific
        if 'arxiv.org' in url:
            abstract_div = soup.find('blockquote', class_='abstract')
            if abstract_div:
                abstract = abstract_div.text.replace('Abstract:', '').strip()

        if not abstract:
            abstract = soup.get_text()[:2000]  # fallback: first 2k characters
        return abstract
    except Exception as e:
        return f"Error scraping {url}: {e}"

# Run Replicate LLM
def generate_summary(text, prompt_type="summary"):
    if prompt_type == "summary":
        prompt = f"Summarize the following academic text:\n\n{text}\n\nSummary:"
    elif prompt_type == "hypothesis":
        prompt = f"Based on this text, suggest a research hypothesis:\n\n{text}\n\nHypothesis:"
    else:
        prompt = text

    try:
        output = client.run(
            f"{REPLICATE_MODEL}:{REPLICATE_VERSION}",
            input={"prompt": prompt, "temperature": 0.7, "max_tokens": 512}
        )
        return "".join(output)
    except Exception as e:
        return f"LLM Error: {e}"

# PDF Text Extraction using PyMuPDF
def extract_pdf_text(uploaded_file):
    try:
        with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
            text = ""
            for page in doc:
                text += page.get_text()
            return text.strip()
    except Exception as e:
        return f"PDF Extraction Error: {e}"

# UI Starts here
st.set_page_config("🧠 Research Agent", layout="wide")
st.title("🧠 Research Agent – Literature Search, Summarization, and PDF Reader")

# --- Section 1: Research Search ---
st.header("🔍 Search & Summarize Research Papers")
query = st.text_input("Enter a research question or topic:")
if st.button("Search and Summarize") and query:
    with st.spinner("Searching and summarizing..."):
        urls = search_papers(query)
        if not urls:
            st.warning("No papers found.")
        else:
            for i, url in enumerate(urls, 1):
                st.markdown(f"### {i}. [Paper Link]({url})")
                abstract = scrape_abstract(url)
                summary = generate_summary(abstract)
                st.markdown("**🔹 Summary:**")
                st.markdown(summary)
                st.markdown("---")

# --- Section 2: PDF Reader & Summarizer ---
st.header("📄 Upload PDF and Summarize")
pdf_file = st.file_uploader("Upload a research paper (PDF)", type=["pdf"])
if pdf_file:
    with st.spinner("Extracting text from PDF..."):
        pdf_text = extract_pdf_text(pdf_file)
    st.success("PDF extracted successfully.")
    
    if st.button("Summarize PDF"):
        with st.spinner("Generating summary..."):
            summary = generate_summary(pdf_text[:3000])  # Limit input size
            st.subheader("📌 Summary:")
            st.markdown(summary)

    if st.button("Suggest Hypothesis"):
        with st.spinner("Generating hypothesis..."):
            hypothesis = generate_summary(pdf_text[:3000], prompt_type="hypothesis")
            st.subheader("💡 Suggested Hypothesis:")
            st.markdown(hypothesis)