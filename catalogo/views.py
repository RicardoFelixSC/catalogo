from rest_framework import viewsets, filters
from .models import Filme
from .serializers import FilmeSerializer

class FilmeViewSet(viewsets.ModelViewSet):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['genero']

