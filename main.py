from pathlib import Path

def GetInfo_Telegram(list_telegram):
    return f"|{list_telegram:^10}|"
def GetInfo_Pictures(list_pictures):
    return f"Number of Pictures: {count_Pictures}"
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