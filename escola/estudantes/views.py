from rest_framework import viewsets
from rest_framework import permissions
from .serializers import EstudanteSerializer
from estudantes.models import Estudante
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class EstudanteViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API que permite que estudantes sejam visualizados ou editados.
    """
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer
    permission_classes = [permissions.AllowAny]

    # Filters
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['nome', 'cpf', 'rg', 'celular']
    search_fields = ['nome', 'cpf', 'rg', 'celular']
    ordering_fields = ['id', 'nome', 'email', 'celular', 'data_nascimento']
