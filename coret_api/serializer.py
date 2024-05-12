
from rest_framework import serializers
from coret_api.models import coret

class coretserializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    number_of_pages = serializers.IntegerField()
    publish_date = serializers.DateField()
    quantity = serializers.IntegerField()

    def create(self, data):
        return coret.objects.create(**data)