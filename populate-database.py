from datetime import datetime

from mongoengine import Document, EmbeddedDocument, connect
from mongoengine.fields import (DateTimeField, Document, EmbeddedDocumentField,
                                FloatField, IntField, ListField, StringField)

connect('ssbw-project', host='mongo')


class Comentario(EmbeddedDocument):
    autor = StringField(required=True, max_length=120)
    texto = StringField(required=True)
    fecha = DateTimeField(default=datetime.now())


class Libro(Document):
    titulo = StringField(required=True, max_length=120)
    autor = StringField(required=True, max_length=120)
    reseña = StringField(required=True)
    fecha_publicacion = DateTimeField(default=datetime.now())
    comentarios = ListField(EmbeddedDocumentField(Comentario))
    foto = StringField(required=True)
    num_paginas = IntField(required=True)
    genero = ListField(required=True)
    precio = FloatField(required=True)


libro1 = Libro(
    titulo='The Eminence in Shadow, Vol. 1 (light novel)',
    autor='Daisuke Aizawa',
    reseña="Even in his past life, Cid's dream wasn't to become a protagonist or a final boss. He'd rather lie low as a minor character until it's prime time to reveal he's a mastermind...or at least, do the next best thing-pretend to be one! And now that he's been reborn into another world, he's ready to set the perfect conditions to live out his dreams to the fullest. Armed with his overactive imagination, Cid jokingly recruits members to his organization and makes up a whole backstory about an evil cult that they need to take down. Well, as luck would have it, these imaginary adversaries turn out to be the real deal-and everyone knows the truth but him!",
    fecha_publicacion=datetime(year=2020, month=8, day=11),
    comentarios=[
        Comentario(autor='John',
                   texto='Muy bueno',
                   fecha=datetime(year=2020, month=8, day=11)),
        Comentario(autor='Jane',
                   texto='Muy malo',
                   fecha=datetime(year=2020, month=8, day=11))
    ],
    foto="http://placeimg.com/480/640/any",
    num_paginas=224,
    genero=['Fiction', 'Fantasy'],
    precio=20.00)

libro2 = Libro(
    titulo='Strike the Blood, Vol. 22 (light novel)',
    autor='Gakuto Mikumo',
    reseña="To save Avrora, Kojou lays it all on the line and gives up his Fourth Primogenitor powers…but the battle is nowhere near over. The Encroachment of Nod begins, and Shahryar Ren’s true ambitions are revealed: to restore the Deva legacy for world domination! Facing the overwhelming might of the Beast Vassal Warheads, the only option seems to be the destruction of Itogami Island-a task assigned to Yukina Himeragi! Torn between duty and friendship, Yukina is tormented by the decision she is forced to make. Things seem dire, but Kojou Akatsuki’s not done yet! There are other ways for him to gain power… and he’s determined to rescue Avrora from Nod. With the support of primogenitors, Attack Mages, Mogwai, and more, he and his friends brace themselves for the battle that will decide the fate of the world.",
    fecha_publicacion=datetime(year=2022, month=11, day=22),
    comentarios=[
        Comentario(autor='John',
                   texto='Muy bueno',
                   fecha=datetime(year=2022, month=12, day=11)),
        Comentario(autor='Jane',
                   texto='Muy malo',
                   fecha=datetime(year=2022, month=12, day=13))
    ],
    foto="http://placeimg.com/480/640/any",
    num_paginas=304,
    genero=['Fiction', 'Science Fiction', 'Action & Adventure'],
    precio=15.00)

libro1.save()
libro2.save()
