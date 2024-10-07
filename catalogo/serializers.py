from rest_framework import serializers
from .models import Filme

class FilmeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filme
        fields = '__all__'

    def validate_ano(self, value):
        if value < 1888 or value > 2100:  # Considerando que o primeiro filme foi feito em 1888
            raise serializers.ValidationError("O ano do filme deve estar entre 1888 e 2100.")
        return value
