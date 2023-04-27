from datetime import datetime, timedelta
from libreria.models import Libro
from rest_framework import serializers

class LibroSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    author = serializers.CharField(max_length=120)
    genre = serializers.CharField(max_length=120)
    description = serializers.CharField(max_length=240)
    isbn = serializers.CharField(max_length=13)
    published = serializers.DateTimeField(default=datetime.now)
    publisher = serializers.CharField(max_length=120)
    # image = serializers.FileField()

    # Suma un día porque mongoengine lo guarda con un día menos al tener en cuenta la hora 00:00:00 según ISO 8601 y el navegador ignorarlo.
    def create(self, validated_data):
        validated_data['published'] = validated_data.get('published')+timedelta(days=1)
        return Libro.objects.create(**validated_data).save()

    def update(self, instance, validated_data):
        if validated_data.get('title'):
            instance.title = validated_data.get('title', instance.title)
        if validated_data.get('author'):
            instance.author = validated_data.get('author', instance.author)
        if validated_data.get('genre'):
            instance.genre = validated_data.get('genre', instance.genre)
        if validated_data.get('description'):
            instance.description = validated_data.get('description', instance.description)
        if validated_data.get('isbn'):
            instance.isbn = validated_data.get('isbn', instance.isbn)
        if validated_data.get('published'):
            # Suma un día porque mongoengine lo guarda con un día menos al tener en cuenta la hora 00:00:00 según ISO 8601 y el navegador ignorarlo.
            instance.published = validated_data.get('published', instance.published)+timedelta(days=1)
        if validated_data.get('publisher'):
            instance.publisher = validated_data.get('publisher', instance.publisher)
        # instance.image = validated_data.get('image', instance.image)
        instance.save()
        # Se vuelve a la fecha original, ya que la respuesta de la API REST si trata la fecha completa correctamente.
        instance.published-=timedelta(days=1)
        return instance