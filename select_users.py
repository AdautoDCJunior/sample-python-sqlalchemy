from db.models.UserModel import UserModel
from db.connection import session

users = session.query(UserModel).all()

print(users)

user = session.query(UserModel).filter_by(id=2).first()

print(user)

for user in session.query(UserModel.name, UserModel.genere):
    print(user)
