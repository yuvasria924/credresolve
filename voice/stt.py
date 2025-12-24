import speech_recognition as sr

def tamil_stt():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ பேசுங்கள்...")
        audio = r.listen(source)
    try:
        return r.recognize_google(audio, language="ta-IN")
    except:
        return None
