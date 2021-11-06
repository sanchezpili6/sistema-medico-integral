from history.models import History
from prescription.models import Prescription
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


class RetrievePrescriptionSerializer(serializers.ModelSerializer):
 
    treatments = serializers.SerializerMethodField()
    certificate = serializers.SerializerMethodField()


    class Meta:
        model = Prescription
        fields = [
            'pk',
            'patient',
            'doctor',
            'medicine',
            'treatments',
            'certificate'
        ]

    def get_treatments(self, instance):

        response_treatments = {}
        response = ""
        doctor = instance.doctor
        patient = instance.patient
        treatments = History.objects.filter(
            doctor=doctor,
            patient=patient
        )
        for treatement in treatments.iterator():
            response += (treatement.treatment)+','

        response_treatments['treatment'] = response 
        return response_treatments

    def get_certificate(self, instance):
        return instance.doctor.certificate


        