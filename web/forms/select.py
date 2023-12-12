from wtforms import SelectField, SubmitField
from flask_wtf import FlaskForm
from sqlalchemy import select

from db.db_session import create_session
from models.horoscope import Horoscope


class SelectForm(FlaskForm):
    date = SelectField("Дата", choices=[])
    zodiac_sign = SelectField("Знак зодиака",
                              choices=[(0, "Овен"), (1, "Телец"), (2, "Близнецы"), (3, "Рак"), (4, "Лев"), (5, "Дева"),
                                       (6, "Весы"), (7, "Скорпион"), (8, "Стрелец"), (9, "Козерог"), (10, "Водолей"),
                                       (11, "Рыбы")])

    def set_choices(self):
        with create_session() as db:
            dates = list(set(db.scalars(select(Horoscope.date)).all()))
        self.date.choices = [(i, dates[i]) for i in range(len(dates))]

    submit_btn = SubmitField("Показать")
