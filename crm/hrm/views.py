from rest_framework import viewsets
from rest_framework import permissions
from django.http import HttpResponse
from hrm.serializers import DesignationSerializer
from hrm.models import Designation


def index(request):
    return HttpResponse('Success')


class DesignationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Designation to be viewed or edited.
    """
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer
    permission_classes = [permissions.IsAuthenticated]