from rest_framework import generics
from shop.models import Product
from shop_api.auth import CustomTokenAuthentication
from shop_api.pagination import CustomPagination
from shop_api.serializers import ProductSerializer, ProductModelSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.authentication import TokenAuthentication

# @csrf_exempt
# def product_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         products = Product.objects.all()
#         serializer = ShopSerializer(products, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = ShopSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
# class ProductList(APIView):
#     """
#     List all snippets, or create a new snippet.
#     """
#     def get(self, request, format=None):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# class ProductDetail(APIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#     def get_object(self, pk):
#         try:
#             return Product.objects.get(pk=pk)
#         except Product.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         product = self.get_object(pk)
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         product = self.get_object(pk)
#         serializer = ProductSerializer(product, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         product = self.get_object(pk)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
# class ProductList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductModelSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
# class ProductDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductModelSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

class ProductList(generics.ListCreateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer

    filter_backends = [DjangoFilterBackend,SearchFilter, OrderingFilter]
    filterset_fields = ['category', 'is_available']
    search_fields = ["name","provider__name","count_items"]
    ordering_fields = ['name', 'category',"price"]
    ordering = ['id']
    pagination_class = CustomPagination
    permission_classes = [DjangoModelPermissions]
    # authentication_classes = [CustomTokenAuthentication]

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
