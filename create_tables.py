from db.connection import base, engine
from db.models.UserModel import UserModel

base.metadata.drop_all(engine)
base.metadata.create_all(engine)
