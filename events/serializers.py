from rest_framework import serializers
from events.models import Event


class EventSerializer(serializers.ModelSerializer):


    client_last_name = serializers.SerializerMethodField()
    client_first_name = serializers.SerializerMethodField()
    client_id = serializers.StringRelatedField()

    class Meta:
        model = Event
        fields = '__all__'

    def get_client_first_name(self, obj):
        return obj.client.first_name

    def get_client_last_name(self, obj):
        return obj.client.last_name
    #
    def get_client_id(self, obj):
        return obj.client.id
