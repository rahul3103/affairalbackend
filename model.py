import os
import datetime
from peewee import Model, PostgresqlDatabase, CharField, DateTimeField,\
    IntegerField, TextField, BigIntegerField
from playhouse.db_url import connect
import settings

if os.environ.get('DATABASE_URL'):
    database = connect(os.environ.get('DATABASE_URL'))
else:
    database = PostgresqlDatabase(
        settings.DB_NAME,
        user=settings.DB_USER,
        password=settings.DB_PASS,
        host=settings.DB_HOST,
        )


class BaseModel(Model):
    class Meta:
        database = database


class Users(BaseModel):
    name = CharField()
    mobile = BigIntegerField()
    email = CharField()
    idcard = TextField()
    rtype = CharField()
    tickets = IntegerField()
    rdate = DateTimeField(default=datetime.datetime.now)


class Event(BaseModel):
    name = CharField()
    edate = DateTimeField()
    etype = CharField()
    location = CharField()


# class Admin(BaseModel):
#     name = CharField()
#     email = CharField(null=False)
#     password_hash = CharField()

#     @property
#     def password(self):
#         raise AttributeError('Password is not readable')

#     @password.setter
#     def password(self, password):
#         self.password_hash = generate_password_hash(password)

#     def verify_password(self, password):
#         return check_password_hash(self.password_hash, password)
