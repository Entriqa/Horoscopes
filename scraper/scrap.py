import datetime
import sys

from bs4 import BeautifulSoup
from requests import get
from sqlalchemy import select

from models import db_session, horoscope


class Parser:
    resource_link = "https://astroscope.ru/horoskop/ejednevniy_goroskop/"
    list_of_horoscopes_links = []
    zodiac_signs_information = []

    def get_horoscopes_links(self):
        request = get_html(self.resource_link)
        soup = BeautifulSoup(request, "html.parser")

        for a in soup.find_all('a', href=True):
            href = a['href']
            if href.startswith("//astroscope.ru/horoskop/ejednevniy_goroskop/") and href.endswith(
                    ".html") and href not in self.list_of_horoscopes_links:
                self.list_of_horoscopes_links.append(href)

        if "//astroscope.ru/horoskop/ejednevniy_goroskop/zavtra.html" in self.list_of_horoscopes_links:
            self.list_of_horoscopes_links.remove("//astroscope.ru/horoskop/ejednevniy_goroskop/zavtra.html")

    def get_zodiac_information(self):
        for link_ind in range(len(self.list_of_horoscopes_links)):
            soup = BeautifulSoup(get_html("https:" + self.list_of_horoscopes_links[link_ind]), "html.parser")

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

            self.zodiac_signs_information.append(zodiac_sign)

    def add_astroprognosis_to_db(self):
        if self.zodiac_signs_information:
            with db_session.create_session() as db:
                if db.scalar(select(horoscope.Horoscope).where(
                        horoscope.Horoscope.date == self.zodiac_signs_information[0].date)):
                    ind = 12
                if db.scalar(select(horoscope.Horoscope).where(
                        horoscope.Horoscope.date == self.zodiac_signs_information[-1].date)):
                    ind = 13
                else:
                    ind = 0
                for i in range(ind, len(self.zodiac_signs_information)):
                    db.add(self.zodiac_signs_information[i])
                db.commit()

    def update_db(self):
        try:
            self.get_horoscopes_links()
            self.get_zodiac_information()
            self.add_astroprognosis_to_db()
        except Exception as e:
            print(e, file=sys.stderr)


def get_html(link):
    try:
        request = get(link).content.decode('utf-8')
        return request
    except Exception as e:
        print(e, file=sys.stderr)


def start_parser():
    parser = Parser()
    parser.update_db()
    return parser
