import requests
imp

def SaveData(url, path):
    r = requests.get(url)
    with open(path, "w", encoding="utf-8") as f:
        f.write(r.text)

url = "https://timesofindia.indiatimes.com"
SaveData(url, "data/index.html")
