import datetime

from bs4 import BeautifulSoup
from requests import get
from sqlalchemy import select

from models import horoscope
from models import db_session


# this function get links for zodiac signs today and tomorrow horoscopes
def get_horoscopes_links() -> list:
    request = get_html("https://astroscope.ru/horoskop/ejednevniy_goroskop/")
    soup = BeautifulSoup(request, "html.parser")
    horoscope_links = []

    for a in soup.find_all('a', href=True):
        href = a['href']
        if href.startswith("//astroscope.ru/horoskop/ejednevniy_goroskop/") and href.endswith(
                ".html") and href not in horoscope_links:
            horoscope_links.append(href)

    if "//astroscope.ru/horoskop/ejednevniy_goroskop/zavtra.html" in horoscope_links:
        horoscope_links.remove("//astroscope.ru/horoskop/ejednevniy_goroskop/zavtra.html")

    return horoscope_links


def get_html(link):
    try:
        request = get(link).content.decode('utf-8')
        return request
    except Exception as e:
        print(e)


def get_zodiac_information():
    prognosis_links = get_horoscopes_links()
    zodiac_signs = []
    for link_ind in range(len(prognosis_links)):
        soup = BeautifulSoup(get_html("https:" + prognosis_links[link_ind]), "html.parser")

        name = soup.find("h1").text.split()[-1]
        text = soup.find("p", {"class": "p-3"}).text
        quote_of_the_day = soup.find("p", {"class": "card-text font-italic"}).text
        zodiac_numbers = soup.find("p", {"class": "card-text mb-3"}).text.split("\n")
        vibrating_number = int(zodiac_numbers[0].split(":")[1])
        lucky_numbers = zodiac_numbers[1].split(":")[1].strip()

        zodiac_sign = horoscope.Horoscope()

        if link_ind < 12:
            zodiac_sign.date = datetime.date.today()
        else:
            zodiac_sign.date = (datetime.date.today() + datetime.timedelta(days=1))
        zodiac_sign.name = name
        zodiac_sign.prediction = text
        zodiac_sign.vibrating_number = vibrating_number
        zodiac_sign.lucky_numbers = lucky_numbers
        zodiac_sign.quote = quote_of_the_day

        zodiac_signs.append(zodiac_sign)

    return zodiac_signs


def add_astroprognosis_to_db():
    zodiac_signs = get_zodiac_information()
    with db_session.create_session() as db:
        if db.scalar(select(horoscope.Horoscope).where(horoscope.Horoscope.date == zodiac_signs[0].date)):
            ind = 12
        else:
            ind = 0
        for prediction in zodiac_signs[ind:]:
            db.add(prediction)
        db.commit()