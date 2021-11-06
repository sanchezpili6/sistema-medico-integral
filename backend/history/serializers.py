from rest_framework import serializers

from history.models import History


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        """Define the class behavior"""
        model = History
        fields = '__all__'