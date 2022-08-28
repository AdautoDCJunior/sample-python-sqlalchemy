from db.models.UserModel import UserModel
from db.connection import session

user_1 = UserModel(name='Primeiro', full_name='Primeiro Usuario',
                   genere='M')

session.add(user_1)
session.commit()

user_2 = UserModel(name='Segundo', full_name='Segundo Usuario',
                   genere='F')

user_3 = UserModel(name='Terceiro', full_name='Terceiro Usuario',
                   genere='F')

session.add_all([user_2, user_3])

session.commit()

