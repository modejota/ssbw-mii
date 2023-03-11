from datetime import datetime
from mongoengine import Document
from mongoengine.fields import DateTimeField, Document, StringField


class Libro(Document):
    title = StringField(required=True, max_length=120)
    author = StringField(required=True, max_length=120)
    genre = StringField(required=True, max_length=120)
    description = StringField(required=True, max_length=240)
    isbn = StringField(required=True, max_length=13, unique=True)
    image = StringField(required=True, max_length=240)
    published = DateTimeField(required=True, default=datetime.now)
    publisher = StringField(required=True, max_length=120)
