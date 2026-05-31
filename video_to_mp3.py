#converts the videos to mp3
import os
import subprocess
files=os.listdir("videos")
for file in files:
    print(file)
    name = file.replace(".mp4","")

    tutorial_number = name.split(". ")[0]
    file_name = name.split(". ")[1].split(" -")[0]

    print(tutorial_number, file_name)

    subprocess.run([
        "ffmpeg",
        "-i", f"videos/{file}",
        f"audios/{tutorial_number}_{file_name}.mp3"
    ])


    



