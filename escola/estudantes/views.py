from rest_framework import viewsets
from rest_framework import permissions
from .serializers import EstudanteSerializer
from estudantes.models import Estudante


class EstudanteViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API que permite que estudantes sejam visualizados ou editados.
    """
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer
    permission_classes = [permissions.AllowAny]
