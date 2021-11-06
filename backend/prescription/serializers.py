from rest_framework import serializers

from prescription.models import Prescription


class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        """Define the class behavior"""
        model = Prescription
        fields = '__all__'

class RetrievePrescriptionSerializer(serializers.ModelSerializer):
 
    treatment = serializers.SerializerMethodField()
    certificate = serializers.SerializerMethodField()


    class Meta:
        model = Prescription
        fields = [
            'patient',
            'doctor',
            'medicine',
            'treatment',
            'certificate'
        ]

    def get_treatment(self, instance):
        

    def get_certificate(self, instance):
        