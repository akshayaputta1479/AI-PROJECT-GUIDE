import os
import requests


def ask_gemini(question):
    key=os.getenv("GEMINI_API_KEY")
    if not key:
        return "**Gemini is not configured.** Add `GEMINI_API_KEY` to `.env` and restart the app."
    try:
        from google import genai
        client=genai.Client(api_key=key)
        response=client.models.generate_content(model="gemini-2.5-flash", contents=question)
        return response.text or "Gemini returned an empty response."
    except Exception as exc:
        return f"**Gemini error:** {exc}"


def ask_ollama(question):
    url=os.getenv("OLLAMA_URL", "http://localhost:11434/api/generate")
    model=os.getenv("OLLAMA_MODEL", "llama3.2")
    try:
        response=requests.post(url, json={"model":model,"prompt":question,"stream":False}, timeout=60)
        response.raise_for_status()
        return response.json().get("response", "Ollama returned an empty response.")
    except Exception as exc:
        return f"**Ollama error:** {exc}. Make sure Ollama is running and the model is available."
