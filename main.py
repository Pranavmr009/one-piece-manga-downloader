import requests
from pyhtml2pdf import converter
from bs4 import BeautifulSoup
import os
import threading

url = "https://ww9.readonepiece.com/chapter/one-piece-digital-colored-comics-chapter-"
url1 = "https://ww9.readonepiece.com/manga/one-piece-digital-colored-comics/"


def main():

    r = requests.get(url1).content
    soup = BeautifulSoup(r, 'html.parser')

    chapters = (soup.find("div", class_="col-span-3").text)

    latest = chapters[0:49]
    split_title = latest.split()

    chapter_number = int(split_title[-1])

    print(chapter_number)

    for chapter in range(chapter_number + 1):
        # formatted_chapter = chapter + 1  # Add 1 to start from chapter 1 instead of 0
        if chapter < 10:
            chapter = str("00" + str(chapter))
        elif chapter < 100:
            chapter = str("0" + str(chapter))

        else:
            chapter = str(chapter)

        chapter_url = f"{url}{chapter}"
        target = f"/media/pranav/HDD-1/one-piece-manga/One-piece-{chapter}.pdf"

        if os.path.exists(target) and os.path.exists(target):
            pass

        else:

            converter.convert(f"{chapter_url}", target=target)

for i in range(20):
    t = threading.Thread(target=main)
    t.start()