# Generated by Django 4.2 on 2024-02-14 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_verify_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='verify_code',
            field=models.CharField(default='282115', max_length=6, verbose_name='Код верификации'),
        ),
    ]
