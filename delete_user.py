from db.models.UserModel import UserModel
from db.connection import session


user = session.query(UserModel).filter_by(id = 1).first()

session.delete(user)

for user in session.query(UserModel).filter_by(name = 'Segundo'):
  session.delete(user)

session.commit()