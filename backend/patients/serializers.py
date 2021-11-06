from rest_framework import serializers

from patients.models import Patient


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        """Define the class behavior"""
        model = Patient
        fields = '__all__'