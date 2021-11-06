from app.urls import router

from utils.mixins import (
    BaseGenericViewSet,
    ListModelMixin,
)

from rest_framework.response import Response
from rest_framework import mixins, status, viewsets
from rest_framework.permissions import AllowAny
from history import serializers


class HistoryViewSet(viewsets.GenericViewSet,
                     BaseGenericViewSet):

    serializer_class = serializers.HistorySerializer

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
    r'history/create',
    HistoryViewSet,
    basename="history"
)

