from rest_framework import viewsets
from livros_app.api import serializers
from livros_app import models


class LivrosViewSet(viewsets.ModelViewSet):
    #serializers_class = serializers.LivrosSerializers
    queryset = models.Livros.objects.all()

    def get_serializer_class(self):
        return serializers.LivrosSerializers