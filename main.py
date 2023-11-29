import datetime

from web.web import app
from models import db_session
from scraper.scrap import add_astroprognosis_to_db

if __name__ == '__main__':
    db_session.global_init("data/database.db")
    # add_astroprognosis_to_db()

    app.run(debug=False)
    print(datetime.datetime.now())
