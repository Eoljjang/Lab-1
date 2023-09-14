import requests

print(requests.__version__)

#resp1 = requests.get("http://google.com")
resp = requests.get("https://raw.githubusercontent.com/Eoljjang/Lab-1/main/script.py")
r = requests.get("https://www.google.ca/")

print(resp.text)
