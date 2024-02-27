from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.models import Product, Shop
from backend.serializers import ProductSerializer


# Create your views here.
class ProductView(APIView):

    def get(self, request, *args, **kwargs):
        shop = Shop.objects.create(name='Svyaznoi', state=True)
        Product.objects.create(name='iphone',
                               category='phones',
                               quantity=20,
                               price=80000,
                               shop=shop)
        queryset = Product.objects.all().select_related('shop')
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(selfself, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            product = serializer.save()
            return Response(ProductSerializer(product).data)
        else:
            return Response(serializer.errors)
