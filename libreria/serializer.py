from datetime import datetime
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

    def create(self, validated_data):
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
            instance.published = validated_data.get('published', instance.published)
        if validated_data.get('publisher'):
            instance.publisher = validated_data.get('publisher', instance.publisher)
        # instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance