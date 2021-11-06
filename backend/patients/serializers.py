from rest_framework import serializers

from patients.models import Patient


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        """Define the class behavior"""
        model = Patient
        fields = '__all__'

class ListPatientSerializer(serializers.ModelSerializer):
    class Meta:
        """Define the class behavior"""
        model = Patient
        fields = [
            'pk',
            'name',
            'nss'
        ]