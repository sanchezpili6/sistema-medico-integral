from app.urls import router

from patients.models import Patient

from rest_framework import mixins, status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from patients import serializers

from utils.mixins import (
    BaseGenericViewSet,
)


class PatientViewSet(viewsets.GenericViewSet,
                     BaseGenericViewSet):

    serializer_class = serializers.PatientSerializer

    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            data=serializer.data,
            status=status.HTTP_201_CREATED
        )




        

router.register(
    r'patient/create',
    PatientViewSet,
    basename="patient"
)
