from app.urls import router

from utils.mixins import (
    BaseGenericViewSet,
    ListModelMixin,
    RetrieveModelMixin,
)

from rest_framework.response import Response
from rest_framework import mixins, status, viewsets
from rest_framework.permissions import AllowAny

from prescription import serializers


# class PrescriptionViewSet(viewsets.GenericViewSet,
#                           BaseGenericViewSet):

#     serializer_class = serializers.PrescriptionSerializer

#     retrieve_serializer_class = serializers.RetrievePrescriptionSerializer

#     permission_classes = [AllowAny]

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         prescription = serializer.save()

        # response_serializer = self.get_serializer(prescription, action='retrieve')
#         return Response(
#             data=response_serializer.data,
#             status=status.HTTP_201_CREATED
#         )


# router.register(
#     r'prescription/create',
#     PrescriptionViewSet,
#     basename="prescription"
# )