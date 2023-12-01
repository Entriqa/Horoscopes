import schedule
import time
import os

import sqlalchemy

from models import db_session
from scrap import start_parser

if __name__ == '__main__':
    db_connection = (f"postgresql+psycopg2://"
                     f"{os.getenv('POSTGRES_USER')}:"
                     f"{os.getenv('POSTGRES_PASSWORD')}@"
                     f"{os.getenv('POSTGRES_HOST')}:"
                     f"{os.getenv('POSTGRES_PORT')}/"
                     f"{os.getenv('POSTGRES_USER')}")

    while True:
        try:
            db_session.global_init(db_connection)
            break
        except sqlalchemy.exc.OperationalError as e:
            print("Problem with db connection")

    parser = start_parser()
    schedule.every().day.at("01:00").do(parser.update_db)

    while True:
        try:
            schedule.run_pending()
            time.sleep(10)
        except Exception:
            print("Schedule exception")
