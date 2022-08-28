from sqlalchemy import Column, Integer, String
from ..connection import base


class UserModel(base):
    __tablename__ = 'usuario'

    id = Column('id', Integer, primary_key=True)
    name = Column('nome', String(50))
    full_name = Column('nomCompleto', String(50))
    genere = Column('genero', String(1))

    def __repr__(self):
        return(
          f'<User(name={self.name}, '
          f'full_name={self.full_name}, '
          f'genere={self.genere})>')