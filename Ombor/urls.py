from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from Asosiy.views import *
from rest_framework_simplejwt.views import TokenRefreshView,TokenObtainPairView


router = DefaultRouter()
router.register("ombor",OmborVIEW)
router.register("mahsulot",MahsulotVIEW)
router.register("client",ClientVIEW)


urlpatterns = [
    path('get_token/', TokenObtainPairView.as_view()),
    path('token_refresh/', TokenRefreshView.as_view()),
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
