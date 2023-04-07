from rest_framework import serializers
from .models import *

class OmborSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ombor
        fields = '__all__'


class MahsulotSerializers(serializers.Serializer):
    class Meta:
        model = Mahsulot
        fields = '__all__'


class ClientSerializers(serializers.Serializer):
    class Meta:
        model = Client
        fields = '__all__'
