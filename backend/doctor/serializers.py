from rest_framework import serializers

from doctor.models import Doctor, Team

from patients.models import Patient

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

