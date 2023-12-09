import os

import sqlalchemy

from web import app
from web.db import db_session

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

    app.run(debug=False, host='0.0.0.0', port=3000)
