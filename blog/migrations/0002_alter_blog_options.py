# Generated by Django 5.0 on 2024-01-09 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ('date_of_create',), 'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
    ]
