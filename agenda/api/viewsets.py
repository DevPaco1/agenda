from rest_framework import viewsets, response
from . import models, serializers
from rest_framework.response import Response

class UserViewSet(viewsets.ViewSet):
    """User sign up"""

   # authentication_classes = []
   # permission_classes = []
    serializer_class = serializers.UserModelSerializer

    def create(self, request):
        """Create new user action"""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return response.Response(
            {"detail": f"user {user.username} created"}, status=201
        )
    def list(self, request):
        queryset = models.User.objects.all()
        serializer_class = serializers.UserModelSerializer(queryset, many=True)
        return Response(serializer_class.data)

class ContactViewSet(viewsets.ModelViewSet):
    """Contact viewset"""

    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactModelSerializer

  