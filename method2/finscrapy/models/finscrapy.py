from mongoengine import *
from app import app

connect('finscrapy', host=app.config['MONGODB_HOST'], port=app.config['MONGODB_PORT'])

class FR(Document):
    meta = {'collection': 'FR'}
    date = StringField()
    title = StringField()
    href = StringField()
    content = StringField()

class ECB(Document):
    meta = {'collection': 'ECB'}
    date = StringField()
    title = StringField()
    href = StringField()
    content = StringField()