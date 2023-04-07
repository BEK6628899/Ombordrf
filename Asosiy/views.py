from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import *
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import *
from .models import *



class OmborVIEW(ModelViewSet):
    queryset = Ombor.objects.all()
    serializer_class = OmborSerializers
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def get_queryset(self):
        queryset = Ombor.objects.filter(user=self.request.user)
        return queryset
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return Response(serializer.data)


class MahsulotVIEW(ModelViewSet):
    queryset = Mahsulot.objects.all()
    serializer_class = MahsulotSerializers
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def get_queryset(self):
        queryset = Mahsulot.objects.filter(ombor__user=self.request.user)
        return queryset
    def perform_create(self, serializer):
        serializer.save(ombor__user=self.request.user)
        return Response(serializer.data)


class ClientVIEW(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializers
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def get_queryset(self):
        queryset = Client.objects.filter(ombor__user=self.request.user)
        return queryset
    def perform_create(self, serializer):
        serializer.save(ombor__user=self.request.user)
        return Response(serializer.data)

    