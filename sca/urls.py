from django.contrib import admin
from django.urls import path, include
from aplic.views import PetsViewSet, UsuariosViewSet, OngsViewSet, EnderecosViewSet, VacinasViewSet, IndexView
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'api/pets', PetsViewSet)
router.register(r'api/usuarios', UsuariosViewSet)
router.register(r'api/ongs', OngsViewSet)
router.register(r'api/enderecos', EnderecosViewSet)
router.register(r'api/vacinas', VacinasViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)), 
    # path('', include('aplic.urls')), Rodar html
]
