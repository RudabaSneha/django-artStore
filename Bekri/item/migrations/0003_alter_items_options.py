# Generated by Django 4.2.3 on 2023-07-24 23:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_alter_category_options_items'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='items',
            options={'verbose_name_plural': 'Items'},
        ),
    ]