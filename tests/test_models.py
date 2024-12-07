def test_read_product(self):
    product = Product.objects.create(name="Test Product")
    fetched_product = Product.objects.get(name="Test Product")
    self.assertEqual(fetched_product.name, "Test Product")
def test_update_product(self):
    product = Product.objects.create(name="Test Product")
    product.name = "Updated Product"
    product.save()
    updated_product = Product.objects.get(id=product.id)
    self.assertEqual(updated_product.name, "Updated Product")
def test_delete_product(self):
    product = Product.objects.create(name="Test Product")
    product.delete()
    with self.assertRaises(Product.DoesNotExist):
        Product.objects.get(name="Test Product")
def test_list_all_products(self):
    Product.objects.create(name="Product 1")
    Product.objects.create(name="Product 2")
    products = Product.objects.all()
    self.assertEqual(len(products), 2)
def test_find_by_name(self):
    product = Product.objects.create(name="Test Product")
    found_product = Product.objects.get(name="Test Product")
    self.assertEqual(found_product.name, "Test Product")
def test_find_by_category(self):
    product = Product.objects.create(name="Test Product", category="Electronics")
    found_product = Product.objects.filter(category="Electronics").first()
    self.assertEqual(found_product.category, "Electronics")
def test_find_by_availability(self):
    product = Product.objects.create(name="Test Product", availability=True)
    found_product = Product.objects.filter(availability=True).first()
    self.assertTrue(found_product.availability)
