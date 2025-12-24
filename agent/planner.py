def plan(user_text):
    if not user_text:
        return "RETRY"
    if "திட்டம்" in user_text or "விண்ணப்பிக்க" in user_text:
        return "COLLECT"
    return "EXECUTE"


