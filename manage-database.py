
import json, requests, argparse
from datetime import datetime

from mongoengine import Document, connect
from mongoengine.fields import DateTimeField, Document, StringField


class Libro(Document):
    title = StringField(required=True, max_length=120)
    author = StringField(required=True, max_length=120)
    genre = StringField(required=True, max_length=120)
    description = StringField(required=True, max_length=240)
    isbn = StringField(required=True, max_length=13, unique=True)
    image = StringField(required=False, max_length=240)
    published = DateTimeField(required=True, default=datetime.now)
    publisher = StringField(required=True, max_length=120)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Database utilities')
    parser.add_argument('action', choices=['populate', 'backup', 'restore'], help='Action to perform')
    parser.add_argument('--file', help='Path to the file for backup or restore')
    # Makefile's call to backup and restore will be like: make backup-datbase ARGS="--file X.json"

    args = parser.parse_args()
    if args.file and not args.file.endswith('.json'):
        args.file.append('.json')

    connect('ssbw-project', host='mongo')

    if args.action == 'populate':
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
                published=libro['published'],
                publisher=libro['publisher']
            )
            libros.append(newlibro)
        Libro.objects.insert(libros, load_bulk=False)

    elif args.action == 'backup':
        if args.file:
            with open(args.file, 'w') as f:
                for document in Libro.objects.all():
                    document_dict = document.to_mongo().to_dict()
                    document_dict.pop('_id')    # Won't be needed when restoring. ISBN is unique
                    document_dict['published'] = document_dict['published'].isoformat()
                    f.write(json.dumps(document_dict) + '\n')
        else:
            print('Please specify a file where to save the backup')

    elif args.action == 'restore':
        if args.file:
            with open(args.file) as f:
                for line in f:
                    doc = json.loads(line)
                    doc['published'] = datetime.fromisoformat(doc['published'])
                    Libro.objects.create(**doc)
        else:
            print('Please specify a file where to restore the backup from')
