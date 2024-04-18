from rest_framework import generics
from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer
from rest_framework.generics import get_object_or_404


# LISTAR E CRIAR
class CursosAPIView(generics.ListCreateAPIView):

    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

#ATUALIZA E DESTROI
class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

# LISTAR E CRIAR
class AvaliacoesAPIView(generics.ListCreateAPIView):

    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_queryset(self):
        if self.kwargs.get('curso_pk'):
            return self.queryset.filter(curso_id=self.kwargs.get('curso_pk'))
        return self.queryset.all()

#ATUALIZA E DESTROI
class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_queryset(self):
        if self.kwargs.get('curso_pk'):
            return get_object_or_404(
                self.get_queryset(),
                curso_id=self.kwargs.get('curso_id'),
                pk=self.kwargs.get('avaliacao_pk')
            )
        return get_object_or_404(
            self.get_queryset(),
            pk=self.kwargs.get('avaliacao_pk')
        )
            
        return self.queryset.all()