import json
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
    isbn = StringField(required=True, max_length=13, unique=True)
    image = StringField(required=True, max_length=240)
    published = DateTimeField(required=True, default=datetime.now)
    publisher = StringField(required=True, max_length=120)

# To be parametrized
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

    """
    with open('my_database_backup.json', 'w') as f:
        for document in Libro.objects.all():
            document_dict = document.to_mongo().to_dict()
            document_dict['_id'] = str(document_dict['_id'])  # Convert _id to string representation
            document_dict['published'] = document_dict['published'].isoformat()
            f.write(json.dumps(document_dict) + '\n')

    with open('my_database_backup.json') as f:
        for line in f:
            doc = json.loads(line)
            doc.pop('_id')
            doc['published'] = datetime.fromisoformat(doc['published'])
            Libro.objects.create(**doc)
    """