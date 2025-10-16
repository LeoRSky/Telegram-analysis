from pathlib import Path

path_telegram = Path(r"C:\Users\User\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Telegram Desktop\Telegram.lnk")

Pictures = (".png", ".jpg", ".jpeg", ".gif")
Videos = (".mp4", ".mov", ".avi", ".mkv")
Audio = (".mp3", ".wav", ".aiff")
Docs = (".docs", ".docx", ".txt", ".pdf", ".ppt", ".pptx",".rar",".zip")

count_Pictures = count_Videos = count_Audio = count_Docs = 0

for file in path_telegram.iterdir():
    if file.is_file():
        name = file.suffix.lower()
        if name in Pictures:
            count_Pictures += 1
        elif name in Videos:
            count_Videos += 1
        elif name in Audio:
            count_Audio += 1
        elif name in Docs:
            count_Docs += 1