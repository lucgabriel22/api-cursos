from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import (
    CursoAPIView,
    AvaliacaoAPIView,
    CursosAPIView,
    AvaliacoesAPIView,
    CursosViewSet,
    AvaliacoesViewSet
)


router = SimpleRouter()
router.register('cursos', CursosViewSet)
router.register('avaliacoes', AvaliacoesViewSet)

# URLS DE AVALIAÇÕES
urlpatterns = [
    path('avaliacoes/', AvaliacoesAPIView.as_view(), name='avaliacoes'),
    path('avaliacoes/<int:pk>/', AvaliacaoAPIView.as_view(), name='avaliacao'),
]

# URLS DE CURSOS
urlpatterns += [ 
    path('cursos/', CursosAPIView.as_view(), name='cursos'),
    path('cursos/<int:pk>/', CursoAPIView.as_view(), name='curso'),
    path('cursos/<int:curso_pk>/avaliacoes/', AvaliacoesAPIView.as_view(), name='curso-avaliacoes'),
    path('cursos/<int:curso_pk>/avaliacoes/<int:avaliacao_pk>/', AvaliacaoAPIView.as_view(), name='avaliacao'),
]



