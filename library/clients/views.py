from rest_framework import viewsets
from rest_framework import permissions
from library.clients.serializer import *

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all().order_by('name')
    serializer_class = ClientSerializer
    permission_classes = []