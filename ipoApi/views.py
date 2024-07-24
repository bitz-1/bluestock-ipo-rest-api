from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ipoApi.models import IpoInfo
from ipoApi.serializers import IpoSerializers
from ipoApi.permission import IsAdminUser

class IpoViewSet(viewsets.ModelViewSet):
    queryset = IpoInfo.objects.all()
    serializer_class = IpoSerializers
    permission_classes = [IsAuthenticated, IsAdminUser]
