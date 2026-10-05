# AI Project Guide

A clean Streamlit application for discovering suitable AI/Data Science projects, analyzing PDF project documents, and using optional Gemini/Ollama assistance.

## Python
Python 3.11.9 recommended.

## Run on Windows PowerShell
```powershell
cd AI_Project_Guide
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
streamlit run app.py
```

Open: http://localhost:8501

## Optional Gemini
Copy `.env.example` to `.env` and add your Gemini API key as `GEMINI_API_KEY=...`.

## Optional Ollama
Install/run Ollama separately and make sure the selected model exists. The default model is `llama3.2`.

## Important Windows fix
The core application does not import PyTorch or Sentence Transformers at startup. This is deliberate because a previous Windows Application Control policy blocked `torch\lib\shm.dll`. The core features use Streamlit, pandas, scikit-learn, requests, and pypdf and therefore run without PyTorch.

## Main features
- Project recommendation by skill, level, and domain
- PDF text extraction and chunking
- Built-in project development guide
- Optional Gemini assistant
- Optional Ollama assistant
- Clean Streamlit interface
