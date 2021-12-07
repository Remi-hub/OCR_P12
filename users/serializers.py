from rest_framework import serializers
from users.models import User, Group


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name',)


class UserSerializer(serializers.ModelSerializer):
    # groups = serializers.StringRelatedField(many=True)
    # groups = GroupSerializer(many=True)

    class Meta:
        model = User
        fields = '__all__'

    # def get_groups(self, obj):
    #     return obj.groups.name
