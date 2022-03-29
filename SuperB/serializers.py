from rest_framework.serializers import ModelSerializer
from SuperB.models import Products, Students


class ProductsSerializers(ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


class StudentsSerializers(ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'
