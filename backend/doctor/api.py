from app.urls import router
from doctor.models import Team


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


class TeamViewSet(ListModelMixin,
                  viewsets.GenericViewSet,
                  BaseGenericViewSet):

    permission_classes = [AllowAny]

    list_serializer_class = serializers.ListTeamSerializer

    queryset = Team.objects.all()




router.register(
    r'doctor/create',
    DoctorViewSet,
    basename="doctor"
)

router.register(
    r'doctor/teams',
    TeamViewSet,
    basename="doctor-team"
)

