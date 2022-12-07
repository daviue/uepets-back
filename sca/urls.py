from django.contrib import admin
from django.urls import path, include
from aplic.views import PetsViewSet, UsuariosViewSet, OngsViewSet, EnderecosViewSet, VacinasViewSet, LoginViewSet, IndexView
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


router = routers.DefaultRouter()
router.register(r'api/pets', PetsViewSet)
router.register(r'api/usuarios', UsuariosViewSet)
router.register(r'api/ongs', OngsViewSet)
router.register(r'api/enderecos', EnderecosViewSet)
router.register(r'api/vacinas', VacinasViewSet)
router.register(r'api/login', LoginViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('', include(router.urls)), 
    # path('', include('aplic.urls')), Rodar html
]
