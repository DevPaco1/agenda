from rest_framework import viewsets, response, decorators
from . import models, serializers


class UserViewSet(viewsets.ViewSet):
    """User sign up"""

    authentication_classes = []
    permission_classes = []
    serializer_class = serializers.UserModelSerializer

    def create(self, request):
        """Create new user action"""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return response.Response(
            {"detail": f"user {user.username} created"}, status=201
        )
    
class ContactViewSet(viewsets.ModelViewSet):
    """Contact viewset"""

    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactModelSerializer

  