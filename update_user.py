from db.models.UserModel import UserModel
from db.connection import session

user = session.query(UserModel).filter_by(id = 1).first()

user.full_name = 'Primeiro Modificado'

session.commit()
