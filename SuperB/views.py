from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from SuperB.models import *
from SuperB.serializers import *


class ProductsViewSet(ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializers
    permission_classes = [IsAdminUser]


class StudentsViewSet(ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializers
    permission_classes = [IsAdminUser]


