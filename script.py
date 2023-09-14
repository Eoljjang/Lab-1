import requests

print(requests.__version__)

#resp = requests.get("http://google.com")
resp = requests.get("https://raw.githubusercontent.com/Eoljjang/Lab-1/main/script.py?token=GHSAT0AAAAAACHR3XFIMMUQB5EC6ZPKAZAGZICKCHA")

print(resp.text)