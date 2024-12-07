from behave import given
from myapp.models import Product

@given('a product with name "{name}" and price "{price}"')
def step_impl(context, name, price):
    Product.objects.create(name=name, price=price, category="Category", availability="In Stock")
