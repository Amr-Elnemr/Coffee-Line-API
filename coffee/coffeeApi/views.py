from rest_framework.views import APIView
from django.http import JsonResponse
from coffeeApi.models import Product
from coffeeApi.serializers import MachineSerializer, PodSerializer

# Create your views here.
class ProductList(APIView):
    def get(self, request, type):
        Products = Product.objects.filter(type=type)
        for key, vals in request.GET.lists():
            for v in vals:
                Products = Products.filter(**{key: v})
        if(type == 'machine'):
            serializer = MachineSerializer(Products, many=True)
        else:
            serializer = PodSerializer(Products, many=True)
        return JsonResponse(serializer.data, safe=False)