from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer

# Read Product
def read_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        return Response(ProductSerializer(product).data, status=status.HTTP_200_OK)
    except Product.DoesNotExist:
        return Response({"detail": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

# Update Product
def update_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Product.DoesNotExist:
        return Response({"detail": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

# Delete Product
def delete_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        product.delete()
        return Response({"detail": "Product deleted"}, status=status.HTTP_204_NO_CONTENT)
    except Product.DoesNotExist:
        return Response({"detail": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

# List All Products
def list_all_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# List Products by Name
def list_products_by_name(request, name):
    products = Product.objects.filter(name__icontains=name)
    if products.exists():
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({"detail": "No products found with the given name"}, status=status.HTTP_404_NOT_FOUND)

# List Products by Category
def list_products_by_category(request, category):
    products = Product.objects.filter(category__icontains=category)
    if products.exists():
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({"detail": "No products found in the given category"}, status=status.HTTP_404_NOT_FOUND)

# List Products by Availability
def list_products_by_availability(request, availability_status):
    products = Product.objects.filter(availability=availability_status)
    if products.exists():
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({"detail": "No products found with the given availability status"}, status=status.HTTP_404_NOT_FOUND)

