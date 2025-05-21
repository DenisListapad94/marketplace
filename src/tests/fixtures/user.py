from django.test import TestCase, Client

from authentication.models import CustomUser
from django.contrib.auth.models import Permission

from django.contrib.auth import authenticate

from model_bakery import baker

def get_test_client():
    return Client()


def create_add_product_permission():
    add_product_permission_codename = "add_product"
    permission_obj = Permission.objects.get(
        codename=add_product_permission_codename
    )
    return permission_obj

def create_product():
    product = baker.make('shop.Product')
    return product

def create_admin_user():
    client = get_test_client()

    user_username = "test"
    user_password = "test"

    CustomUser.objects.create_user(
        username=user_username,
        password=user_password,
        is_superuser=True,
    )
    credentials = {
        "username": user_username,
        "password": user_password,
    }
    user = authenticate(username=user_username, password=user_password)

    client.login(**credentials)

    return user, client
