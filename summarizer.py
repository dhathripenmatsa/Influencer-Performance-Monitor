def summarize_text(text: str) -> str:
    """Dummy summarizer (can replace with GPT/OpenAI API later)"""
    if not text:
        return "No description provided."
    return text[:120] + "..." if len(text) > 120 else text
