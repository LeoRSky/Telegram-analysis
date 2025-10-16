from pathlib import Path

def GetInfo_Telegram(list_telegram):
    return f"|{list_telegram:^10}|"
def GetInfo_Pictures(list_pictures):
    return f"Number of Pictures: {count_pictures}"
def GetInfo_Videos(list_videos):
    return f"Number of Videos: {count_videos}"
def GetInfo_Audio(list_audio):
    return f"Number of Audio: {count_audio}"
def GetInfo_Docs(list_docs):
    return f"Number of Docs: {count_docs}"
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

list_Telegram = "Telegram download analysis"
print(GetInfo_Telegram(list_Telegram))
print(GetInfo_Pictures(count_Pictures))
print(GetInfo_Videos(count_Videos))
print(GetInfo_Audio(count_Audio))
print(GetInfo_Docs(count_Docs))
print(f"|{list_Telegram:^10}|")
print(f"Number of Pictures: {count_Pictures}")
print(f"Number of Videos: {count_Videos}")
print(f"Number of Audio: {count_Audio}")
print(f"Number of Documents: {count_Docs}")
