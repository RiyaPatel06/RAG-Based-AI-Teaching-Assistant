import whisper
import os
import json

print("Loading Whisper model...")
model = whisper.load_model("small")   # first time will take time

audio_folder = "audios"
output_folder = "chunks"

# loop through all audio files
for audio in os.listdir(audio_folder):

    if audio.endswith(".mp3"):
        print(f"\nProcessing: {audio}")

        # ---------- metadata from filename ----------
        filename = audio.replace(".mp3", "")
        number = filename.split("_")[0]              # 000
        title = filename.split("_")[1]               # OOP

        # ---------- transcription ----------
        result = model.transcribe(
            audio=f"{audio_folder}/{audio}",
            language="hi",
            task="translate",
            word_timestamps=False
        )

        # ---------- chunk creation ----------
        chunks = []
        for segment in result["segments"]:
            chunk_data = {
                "number": number,
                "title": title,
                "start": segment["start"],
                "end": segment["end"],
                "text": segment["text"]
            }
            chunks.append(chunk_data)

        # ---------- final JSON structure ----------
        final_data = {
            "video_number": number,
            "video_title": title,
            "full_transcript": result["text"],
            "chunks": chunks
        }

        # ---------- save JSON ----------
        output_path = f"{output_folder}/{filename}.json"
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(final_data, f, indent=4, ensure_ascii=False)

        print(f"Saved: {output_path}")

print("\nAll files processed")