import requests

r = requests.get(raw_input())
html = str(r.text)
print r.text