from agent.planner import plan
from agent.executor import run_agent
from agent.memory import Memory
from voice.stt import tamil_stt
from voice.tts import tamil_tts

memory = Memory()
tamil_tts("வணக்கம்! அரசு திட்டம் உதவி முகவருக்கு வரவேற்கிறோம்")

while True:
    user = tamil_stt()

    if not user:
        tamil_tts("குரல் புரியவில்லை, மீண்டும் பேசுங்கள்")
        continue

    act = plan(user)

    if "வயது" in user:
        num = int("".join(filter(str.isdigit, user)))
        memory.update("age", num)
        tamil_tts(f"வயது {num} பதிவு செய்யப்பட்டது")
        continue

    if "வருமானம்" in user:
        num = int("".join(filter(str.isdigit, user)))
        memory.update("income", num)
        tamil_tts(f"வருமானம் {num} பதிவு செய்யப்பட்டது")
        continue

    if "மாணவர்" in user:
        memory.update("category", "student")
        tamil_tts("வகை: மாணவர்")
        continue
    if "பெண்" in user:
        memory.update("category", "woman")
        tamil_tts("வகை: மகளிர்")
        continue
    if "விவசாயி" in user:
        memory.update("category", "farmer")
        tamil_tts("வகை: விவசாயி")
        continue

    out = run_agent(memory)

    if out["status"] == "INCOMPLETE":
        tamil_tts("வயது, வருமானம், வகை சொல்லுங்கள்")
        continue
    if out["status"] == "FAILED":
        tamil_tts("சர்வர் பிழை, மீண்டும் முயற்சி செய்கிறேன்")
        continue
    if out["status"] == "NOT_ELIGIBLE":
        tamil_tts("நீங்கள் தகுதி இல்லை")
        break
    if out["status"] == "SUCCESS":
        tamil_tts(f"{out['scheme']} திட்டத்திற்கு விண்ணப்பம் வெற்றி! எண் {out['app_id']}")
        break

