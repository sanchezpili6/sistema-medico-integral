from history.models import History
from rest_framework import serializers

from doctor.models import Doctor, Team

from patients.models import Patient

from prescription.models import Prescription

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        """Define the class behavior"""
        model = Doctor
        fields = '__all__'

class PatientsSerializer(serializers.ModelSerializer):
    class Meta:
        """Define the class behavior"""
        model = Patient
        fields = '__all__'

class ListDoctorSerializer(serializers.ModelSerializer):

    class Meta:

        model = Doctor
        fields = (
            'name',
            'specialty'
        )

        
class ListTeamSerializer(serializers.ModelSerializer):

    doctor = ListDoctorSerializer(many=True, read_only=True)

    class Meta:
        """Define the class behavior"""
        model = Team
        fields = [
            'pk',
            'doctor'
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
