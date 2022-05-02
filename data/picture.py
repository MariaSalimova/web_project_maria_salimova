import sqlalchemy
from sqlalchemy import orm
from data.db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin


class Picture(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'pictures'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    picture = sqlalchemy.Column(sqlalchemy.LargeBinary, nullable=True)
    artist_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("artists.id"))
    artist = orm.relation('Artist')
    rating = sqlalchemy.Column(sqlalchemy.Integer, default=0)
