from app.urls import router

from patients.models import Patient
from prescription.models import Prescription

from rest_framework import mixins, status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from patients import serializers

from utils.mixins import (
    BaseGenericViewSet,
    ListModelMixin
)


class PatientViewSet(ListModelMixin,
                     viewsets.GenericViewSet,
                     BaseGenericViewSet):

    serializer_class = serializers.PatientSerializer

    permission_classes = [AllowAny]

    list_serializer_class = serializers.ListPatientSerializer

    queryset = Patient.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            data=serializer.data,
            status=status.HTTP_201_CREATED
        )

class PatientLoginViewSet(viewsets.GenericViewSet,
                         BaseGenericViewSet):

    serializer_class = serializers.PatientSerializer

    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        nss = request.data['nss']
        try:
            patient = Patient.objects.get(nss=nss)
        except Patient.DoesNotExist:
            return Response(
                    data={'Paciente no dado de alta'},
                    status=status.HTTP_404_NOT_FOUND
                )
    
        serializer = self.get_serializer(patient)
        return Response(
            data=serializer.data,
            status=status.HTTP_201_CREATED
        )


class PrescriptionsViewSet(ListModelMixin,
                           viewsets.GenericViewSet,
                           BaseGenericViewSet):

    list_serializer_class = serializers.RetrievePrescriptionSerializer

    permission_classes = [AllowAny]

    def get_queryset(self):
        pk = self.request.query_params.get('pk')
        return Prescription.objects.filter(patient=pk) 



router.register(
    r'patient/create',
    PatientViewSet,
    basename="patient"
)

router.register(
    r'patient/login',
    PatientLoginViewSet,
    basename="patient-login"
)

router.register(
    r'patient/prescriptions',
    PrescriptionsViewSet,
    basename="patient-prescriptions"
)


 