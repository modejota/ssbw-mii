from datetime import datetime

import requests
from mongoengine import Document, connect
from mongoengine.fields import DateTimeField, Document, StringField

connect('ssbw-project', host='mongo')


class Libro(Document):
    title = StringField(required=True, max_length=120)
    author = StringField(required=True, max_length=120)
    genre = StringField(required=True, max_length=120)
    description = StringField(required=True, max_length=240)
    isbn = StringField(required=True, max_length=13)
    image = StringField(required=True, max_length=240)
    published = DateTimeField(required=True, default=datetime.now)
    publisher = StringField(required=True, max_length=120)


if __name__ == "__main__":
    response = requests.get('https://fakerapi.it/api/v1/books?_quantity=50')
    data = response.json()
    libros = []
    for libro in data['data']:
        newlibro = Libro(
            title=libro['title'],
            author=libro['author'],
            genre=libro['genre'],
            description=libro['description'],
            isbn=libro['isbn'],
            image=libro['image'],
            published=libro['published'],
            publisher=libro['publisher']
        )
        libros.append(newlibro)
    Libro.objects.insert(libros)