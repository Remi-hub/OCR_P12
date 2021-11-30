from rest_framework import serializers
from events.models import Event


class EventSerializer(serializers.ModelSerializer):

    support_contact = serializers.SerializerMethodField()
    client_last_name = serializers.SerializerMethodField()
    client_first_name = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = '__all__'

    def get_support_contact(self, obj):
        return obj.support_contact.username

    def get_client_first_name(self, obj):
        return obj.client.first_name

    def get_client_last_name(self, obj):
        return obj.client.last_name
