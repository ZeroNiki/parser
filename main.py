from bs4 import BeautifulSoup
from translate import Translator
import requests

translator = Translator(from_lang="en", to_lang="ru")

x = 0
while True:
    if x == 0:
        url = "https://news.ycombinator.com/newest"
    else:
        url = f"https://news.ycombinator.com/newest{next}"
    request = requests.get(url)

    soup = BeautifulSoup(request.text, "html.parser")

    teme = soup.find_all("td", class_="title")

    for temes in teme:
        temes = temes.find("a")
        if temes is not None and 'github.com' in str(temes):
            sublinks = temes.get('href')
            print(f"{str(translator.translate(temes.text))} {str(sublinks)}\n<====>")

    nex = soup.find(class_="morelink")
    nexlink = nex.get("href")

    next = nexlink[6:]
    x = x+1
