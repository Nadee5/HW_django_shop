# Generated by Django 4.2 on 2024-02-16 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blog_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='slug'),
        ),
    ]
