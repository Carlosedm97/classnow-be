from rest_framework import viewsets
from classnowapp.serializers import ClasesSerializer
from classnowapp.models import Clases


class ClasesView(viewsets.ModelViewSet):
    serializer_class = ClasesSerializer
    queryset = Clases.objects.all()
