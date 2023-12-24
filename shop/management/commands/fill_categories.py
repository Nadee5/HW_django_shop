from django.core.management import BaseCommand

from shop.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        category_list = [
            {'name': 'Аудиотехника', 'description': 'Портативное/ домашнее аудио, наушники, автозвук'},
            {'name': 'Техника для кухни', 'description': 'Крупная/ мелкая/ встраиваемая'},
            {'name': 'Техника для дома', 'description': 'Климатическая техника, уход за одеждой'},
            {'name': 'Умный дом', 'description': 'Экосистемы, устройства, умный свет, датчики'},
        ]

        categories_for_create = []
        for category in category_list:
            categories_for_create.append(
                Category(**category)
            )

        Category.objects.all().delete()
        Category.objects.bulk_create(categories_for_create)
