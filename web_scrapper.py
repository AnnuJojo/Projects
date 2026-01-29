import requests
from bs4 import BeautifulSoup

# URL of the article
url = "https://edition.cnn.com/travel/article/scenic-airport-landings-2020/index.html"
r = requests.get(url)

# Write HTML to file using UTF-8
with open("file.html", "w", encoding="utf-8") as f:
    f.write(r.text)

# Read HTML from file using UTF-8
with open("file.html", "r", encoding="utf-8") as f:
    html = f.read()

# Parse with BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Extract Title and Author
print("TITLE:", soup.find("h1").get_text(strip=True))
print("AUTHOR:", soup.find("span", class_="byline__name vossi-byline__name").get_text(strip=True))

print("~"*100)

# Extract article paragraphs
container = soup.find("div", class_="article__content")
paragraphs = container.find_all("p")
for paras in paragraphs:
    print(paras.get_text(strip=True))
    print()
