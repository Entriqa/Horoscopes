import datetime

from sqlalchemy.orm import mapped_column, Mapped

from sqlalchemy_serializer import SerializerMixin

from db import db_session


class Horoscope(db_session.SqlAlchemyBase, SerializerMixin):
    __tablename__ = "horoscopes"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    prediction: Mapped[str]
    lucky_numbers: Mapped[str]
    vibrating_number: Mapped[int]
    quote: Mapped[str]
    date: Mapped[datetime.date]
