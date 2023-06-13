from sqlalchemy import Column, BigInteger, String, sql, Date, Boolean

from utils.db_api.db_gino import TimedBaseModel


class User(TimedBaseModel):
    __tablename__ = 'users'
    id = Column(BigInteger, primary_key=True)
    category = Column(String(100))
    wishes = Column(Boolean)

    query: sql.Select