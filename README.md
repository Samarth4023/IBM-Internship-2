# 🧠 Research Agent

An AI-powered assistant that helps you search for research papers, scrape academic content, summarize it using large language models (LLMs), extract and summarize PDF files, and even generate hypotheses — all in one easy-to-use Streamlit interface.

### 🚀 Features

* 🔍 **Literature Search** from arXiv via DuckDuckGo
* 🌐 **Web Scraping** of abstracts and page content
* 📄 **PDF Reader** with text extraction (via PyMuPDF)
* 🤖 **Summarization & Hypothesis Generation** using `ibm-granite/granite-3.3-8b-instruct` (via Replicate)
* 🧪 Ideal for students, researchers, and academics

---

## 📸 Demo

<img width="1365" height="597" alt="image" src="https://github.com/user-attachments/assets/4a119d6c-97d0-4ec9-b5df-e55dbf8e0bd8" />

---

## 📦 Requirements

Install all dependencies using:

```bash
pip install -r requirements.txt
```

Or individually:

```bash
pip install streamlit replicate requests beautifulsoup4 PyMuPDF
```

---

## 🔑 Replicate API Setup

1. Go to [Replicate API Tokens](https://replicate.com/account/api-tokens)
2. Generate a new API token
3. **Recommended**: Set it as an environment variable

```bash
export REPLICATE_API_TOKEN=your_token_here
```

Or, you can hardcode it (not recommended for production):

```python
REPLICATE_API_TOKEN = "your_token_here"
client = replicate.Client(api_token=REPLICATE_API_TOKEN)
```

---

## 🧠 Model Used

* **Model**: `ibm-granite/granite-3.3-8b-instruct`
* **Version ID**: `3ff9e6e20ff1f31263bf4f36c242bd9be1acb2025122daeefe2b06e883df0996`

You can change the model in `app.py` if needed.

---

## 🖥️ Run the App

Start your Streamlit app locally:

```bash
streamlit run app.py
```

Then go to LocalHost.

---

## ✍️ Example Prompts

```txt
Find three recent research papers on the ethical implications of using CRISPR technology in humans.
Summarize the uploaded paper and highlight the main results and methodology.
Suggest a hypothesis based on the uploaded PDF.
Draft an abstract for a paper on AI in climate modeling.
```

---

## 📁 File Structure

```bash
📦 research-agent/
├── app.py              # Main Streamlit app
├── requirements.txt    # Required libraries
└── README.md           # You're here
```

---

## 🛡️ Disclaimer

* This tool uses third-party APIs and AI models. Use it responsibly for academic and research purposes only.
* Always verify LLM-generated content before citing or using it in official research.

---

## 💡 Future Improvements

* Export to PDF / BibTeX / CSV
* Follow-up Q\&A on paper content
* Semantic search with vector embeddings

---

## 👤 Author

Samarth Pujari

AI Intern @ IBM

Connect with me on [LinkedIn](www.linkedin.com/in/samarth-pujari-328a1326a) | [Kaggle](https://www.kaggle.com/samarthpujari)
