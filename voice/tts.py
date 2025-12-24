from gtts import gTTS
import IPython.display as ipd

def tamil_tts(text):
    tts = gTTS(text, lang="ta")
    file = "out.mp3"
    tts.save(file)
    print("🔊 Agent:", text)
    print("📁 Audio saved as:", file)
# 



