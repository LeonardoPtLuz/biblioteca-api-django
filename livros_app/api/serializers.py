from rest_framework import serializers
from livros_app import models


class LivrosSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Livros
        fields = '__all__'