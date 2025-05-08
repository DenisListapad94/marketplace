from django.core.management.base import BaseCommand
from shop.models import Product
from faker import Faker

class Command(BaseCommand):
    help = "Generate fake products"

    def handle(self, *args, **options):
        faker = Faker()
        product_list = []
        for ind in range(100000):
            product = Product(
                name=faker.text(max_nb_chars=20),
                price=faker.random_int(min=10, max=1000),
                count_items=faker.random_int(min=1, max=50)
            )
            product_list.append(product)
            if ind % 1000 == 0 and product_list:
                Product.objects.bulk_create(product_list)
                product_list = []

        self.stdout.write(self.style.SUCCESS('Successfully created 100000 fake products.'))

