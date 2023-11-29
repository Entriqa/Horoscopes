from datetime import datetime

import flask
from sqlalchemy import select

from web.forms.select import SelectForm
from models.db_session import create_session
from models.horoscope import Horoscope


app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'


@app.route('/', methods=['GET', 'POST'])
def main_page():
    form = SelectForm()
    form.set_choices()
    if form.submit_btn.data:
        zodiac_sign = form.zodiac_sign.choices[int(form.zodiac_sign.data)][1]
        date = form.date.choices[int(form.date.data)][1]
        # print(date)
        return flask.redirect(f"/horoscope{date}:{zodiac_sign}")

    return flask.render_template('index.html', form=form)


@app.route('/horoscope<horoscope>', methods=['GET', 'POST'])
def horoscope_page(horoscope):
    print(horoscope.split(':')[0])
    date = datetime.strptime(horoscope.split(":")[0], "%Y-%m-%d").date()
    # print(date)
    zodiac_sign = horoscope.split(":")[1]
    with create_session() as db:
        prediction = db.scalar(select(Horoscope).where(Horoscope.date == date,
                                                       Horoscope.name == zodiac_sign))

    return flask.render_template('horoscope.html', prediction=prediction)
