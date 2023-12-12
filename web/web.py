from datetime import datetime

import flask
from sqlalchemy import select

from forms.select import SelectForm
from db.db_session import create_session
from models.horoscope import Horoscope


app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_key'


@app.route('/', methods=["POST", "GET"])
def main_page():
    form = SelectForm()
    form.set_choices()
    if form.submit_btn.data:
        zodiac_sign = form.zodiac_sign.choices[int(form.zodiac_sign.data)][1]
        date = form.date.choices[int(form.date.data)][1]
        return flask.redirect(f"/horoscope{date}:{zodiac_sign}")

    return flask.render_template('index.html', form=form)


@app.route('/horoscope<horoscope>', methods=["GET", "POST"])
def horoscope_page(horoscope):
    date = datetime.strptime(horoscope.split(":")[0], "%Y-%m-%d").date()

    zodiac_sign = horoscope.split(":")[1]
    with create_session() as db:
        prediction = db.scalar(select(Horoscope).where(Horoscope.date == date,
                                                       Horoscope.name == zodiac_sign))
    form = SelectForm()
    form.set_choices()
    form.zodiac_sign.s
    if form.submit_btn.data:
        zodiac_sign = form.zodiac_sign.choices[int(form.zodiac_sign.data)][1]
        date = form.date.choices[int(form.date.data)][1]
        # print(date)
        return flask.redirect(f"/horoscope{date}:{zodiac_sign}")

    return flask.render_template('horoscope.html', prediction=prediction, form=form)
