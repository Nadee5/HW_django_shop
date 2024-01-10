from django.core.management import BaseCommand

from shop.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        category_list = [
            {'name': 'Аудиотехника',
             'description': 'Портативное/ домашнее аудио, наушники, автозвук',
             'image': 'category/audio.jpg'},
            {'name': 'Техника для кухни',
             'description': 'Крупная/ мелкая/ встраиваемая',
             'image': 'category/kitchen_appliances.jpg'},
            {'name': 'Техника для дома',
             'description': 'Климатическая техника, уход за одеждой',
             'image': 'category/home_appliances.png'},
            {'name': 'Умный дом',
             'description': 'Экосистемы, устройства, умный свет, датчики',
             'image': 'category/smart_home.jpg'},
        ]

        categories_for_create = []
        for category in category_list:
            categories_for_create.append(
                Category(**category)
            )

        Category.objects.all().delete()
        Category.objects.bulk_create(categories_for_create)
