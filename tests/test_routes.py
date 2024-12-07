def test_read_product_route(self):
    product = Product.objects.create(name="Test Product")
    response = self.client.get(f'/api/products/{product.id}/')
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.data['name'], "Test Product")
