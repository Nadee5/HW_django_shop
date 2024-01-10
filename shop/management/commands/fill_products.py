from django.core.management import BaseCommand

from shop.models import Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        product_list = [
            {'name': 'Наушники',
             'description': 'Полноразмерные',
             'image': 'product/headphones.png',
             'category_id': 1,
             'price_for_one': '5800'},
            {'name': 'Кофемашина',
             'description': 'Автоматическая',
             'image': 'product/coffee_machine.png',
             'category_id': 2,
             'price_for_one': '30000'},
            {'name': 'Робот-пылесос',
             'description': 'Для влажной уборки',
             'image': 'product/robot_vacuum.png',
             'category_id': 3,
             'price_for_one': '34000'},
            {'name': 'Датчик открытия дверей и окон',
             'description': 'Экосистема Яндекс',
             'image': 'product/sensor.png',
             'category_id': 4,
             'price_for_one': '2000'},
        ]

        products_for_create = []
        for product in product_list:
            products_for_create.append(
                Product(**product)
            )

        Product.objects.all().delete()
        Product.objects.bulk_create(products_for_create)
