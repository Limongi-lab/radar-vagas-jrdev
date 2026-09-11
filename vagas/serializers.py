from rest_framework import serializers
from .models import Fonte, Vaga


class FonteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fonte
        fields = "__all__"


class VagaSerializer(serializers.ModelSerializer):
    fonte = serializers.StringRelatedField()

    class Meta:
        model = Vaga
        fields = "__all__"