import whisper
import json

# load model (use base/small if CPU)
model = whisper.load_model("base")

# transcribe audio
result = model.transcribe(
    "audios/000_OOps Fundamentals Introduction.mp3",
    language="hi",
    task="translate"
)

# extract only useful fields
chunks = [
    {
        "start": seg["start"],
        "end": seg["end"],
        "text": seg["text"]
    }
    for seg in result["segments"]
]

# save json
with open("output.json", "w", encoding="utf-8") as f:
    json.dump(chunks, f, indent=4, ensure_ascii=False)

