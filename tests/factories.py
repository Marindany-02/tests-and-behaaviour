import factory
from .models import Product

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product
    
    name = factory.Faker('word')
    category = factory.Faker('word')
    availability = factory.Faker('boolean')
