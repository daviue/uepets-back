from django.contrib import admin
from django.urls import path, include
from aplic.views import PetsViewSet, UsuariosViewSet, OngsViewSet, EnderecosViewSet, VacinasViewSet, IndexView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'pets', PetsViewSet)
router.register(r'usuarios', UsuariosViewSet)
router.register(r'ongs', OngsViewSet)
router.register(r'enderecos', EnderecosViewSet)
router.register(r'vacinas', VacinasViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)), 
    # path('', include('aplic.urls')), Rodar html
]
