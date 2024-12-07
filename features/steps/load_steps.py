from .factories import ProductFactory

@given('the products are loaded')
def step_impl(context):
    ProductFactory.create_batch(5)
