from datetime import datetime
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