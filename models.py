from app import app
from pymodm import connect, MongoModel, fields

connect(app.config.get('PYMODM_HOST'))


class User(MongoModel):
    first_name = fields.CharField()
    last_name = fields.CharField()
    email = fields.EmailField(required=True)
    phone_number = fields.CharField(required=True)
    password = fields.CharField()
    created = fields.DateTimeField()
    updated = fields.DateTimeField()
    last_login = fields.DateTimeField()
    is_admin = fields.BooleanField(default=False)

