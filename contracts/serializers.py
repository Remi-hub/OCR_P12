from rest_framework import serializers
from contracts.models import Contract


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'
        # exclude = ('date_created', )
        # extra_kwargs = {
        #     'date_created': {'read_only': True}
        # }
