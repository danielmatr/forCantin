from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, AllowAny
from SuperB.models import *
from SuperB.serializers import *


class ProductsViewSet(ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializers
    permission_classes = [AllowAny]


class StudentsViewSet(ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializers
    permission_classes = [AllowAny]


