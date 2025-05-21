from django.test import TestCase
from shop.models import Product

from tests.fixtures.user import (
    create_admin_user,
    create_product,
)

class TestShopView(TestCase):

    def setUp(self):
        self.product = create_product()
        self.user, self.client = create_admin_user()

    def test_product_view(self):
        url = "/shop/products"

        response = self.client.get(path=url)
        success_status_code = 200
        self.assertEqual(response.status_code,success_status_code)

        products = response.context["products"]
        self.assertEqual(len(products),1)
        self.assertEqual(products[0].name, self.product.name)
        self.assertEqual(products[0].price, self.product.price)

    def test_create_product(self):
        test_description = "test_description"
        payload = {
            "name":self.product.name,
            "price": self.product.price,
            "count_items": self.product.count_items,
            "description": test_description,
        }

        url = "/shop/add_product"
        response = self.client.post(path=url,data=payload)

        success_status_code = 302
        self.assertEqual(response.status_code,success_status_code)

        products = Product.objects.all()
        self.assertEqual(len(products), 2)
        self.assertEqual(products[1].name, self.product.name)
        self.assertEqual(products[1].price, self.product.price)
        self.assertEqual(products[1].count_items, self.product.count_items)
        self.assertEqual(products[1].description, test_description)
