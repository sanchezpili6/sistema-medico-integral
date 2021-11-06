from app.urls import router
import doctor

from doctor.models import Doctor, Team

from patients.models import Patient

from prescription.models import Prescription


from rest_framework import mixins, status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from doctor import serializers

from utils.mixins import (
    BaseGenericViewSet,
    ListModelMixin,
)


class DoctorViewSet(viewsets.GenericViewSet,
                    BaseGenericViewSet):

    serializer_class = serializers.DoctorSerializer

    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        doctor = serializer.save()
        number_team = request.data['team']
        try:
            team= Team.objects.get(
                number=number_team
            )
        except:
            team = Team.objects.create(number=number_team)
        team.doctor.add(doctor)

        return Response(
            data=serializer.data,
            status=status.HTTP_201_CREATED
        )

class DoctorLoginViewSet(viewsets.GenericViewSet,
                         BaseGenericViewSet):

    serializer_class = serializers.DoctorSerializer

    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        certificate = request.data['certificate']
        try:
            doctor= Doctor.objects.get(certificate=certificate)
        except Doctor.DoesNotExist:
            return Response(
                    data={'Doctor no dado de alta'},
                    status=status.HTTP_404_NOT_FOUND
                )
    
        serializer = self.get_serializer(doctor)
        return Response(
            data=serializer.data,
            status=status.HTTP_201_CREATED
        )

class TeamViewSet(ListModelMixin,
                  viewsets.GenericViewSet,
                  BaseGenericViewSet):

    permission_classes = [AllowAny]

    list_serializer_class = serializers.ListTeamSerializer

    queryset = Team.objects.all()


class PatientsViewSet(ListModelMixin,
                      viewsets.GenericViewSet,
                      BaseGenericViewSet):

    list_serializer_class = serializers.PatientsSerializer

    permission_classes = [AllowAny]

    def get_queryset(self):
        pk = self.request.query_params.get('pk')
        return Patient.objects.filter(doctor=pk)

class PrescriptionsViewSet(ListModelMixin,
                           viewsets.GenericViewSet,
                           BaseGenericViewSet):

    list_serializer_class = serializers.RetrievePrescriptionSerializer

    permission_classes = [AllowAny]

    def get_queryset(self):
        pk = self.request.query_params.get('pk')
        return Prescription.objects.filter(doctor=pk)       


router.register(
    r'doctor/create',
    DoctorViewSet,
    basename="doctor"
)

router.register(
    r'doctor/login',
    DoctorLoginViewSet,
    basename="doctor-login"
)

router.register(
    r'doctor/teams',
    TeamViewSet,
    basename="doctor-team"
)

router.register(
    r'doctor/patients',
    PatientsViewSet,
    basename="doctor-patients"
)

router.register(
    r'doctor/prescriptions',
    PrescriptionsViewSet,
    basename="doctor-prescriptions"
)