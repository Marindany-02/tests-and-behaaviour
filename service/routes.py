def read_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        return Response(ProductSerializer(product).data, status=status.HTTP_200_OK)
    except Product.DoesNotExist:
        return Response({"detail": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
