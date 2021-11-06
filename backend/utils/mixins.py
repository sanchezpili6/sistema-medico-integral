"""Generic mixins."""
from inspect import getmembers

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.settings import api_settings


def _is_extra_action(attr):
    return hasattr(attr, 'mapping')


class BaseGenericViewSet(GenericAPIView):

    """
    The GenericViewSet class does not provide any actions by default.
    But does include the base set of generic view behavior, such as
    the `get_object` and `get_queryset` methods.
    """

    def get_serializer_class(self, action=None):
        """Return the serializer class depending on request method."""

        if action is not None:
            class_name = f'{action}_serializer_class'
            return getattr(self, class_name)
        else:
            return super(BaseGenericViewSet, self).get_serializer_class()

    def get_serializer(self, *args, **kwargs):
        """
        Return the serializer that should be used to the given action.
        If any action was given, returns the serializer_class.
        """
        action = kwargs.pop('action', None)

        serializer_class = self.get_serializer_class(action)

        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)

    @classmethod
    def get_extra_actions(cls):
        """Get the methods that are marked as an extra ViewSet `@action`."""
        return [method for _, method in getmembers(cls, _is_extra_action)]


class ListModelMixin:
    """List a queryset."""
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True, action='list')
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True, action='list')
        return Response(serializer.data)


class CreateModelMixin:
    """Create a model instance."""
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, action='create')
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def perform_create(self, serializer):
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}


class RetrieveModelMixin:
    """Retrieve a model instance."""
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, action='retrieve')
        return Response(serializer.data)


class UpdateModelMixin:
    """Update a model instance."""
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial, action="update"
        )
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)


class DestroyModelMixin:
    """Logical destroy of a model instance."""
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        self.perform_destroy(instance)
        serializer = self.get_serializer(instance, action="destroy")
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def perform_destroy(self, instance):
        instance.save()
