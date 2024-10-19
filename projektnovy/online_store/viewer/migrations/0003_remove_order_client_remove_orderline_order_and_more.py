# Generated by Django 4.1.1 on 2024-10-14 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0002_client_order_orderline'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='client',
        ),
        migrations.RemoveField(
            model_name='orderline',
            name='order',
        ),
        migrations.RemoveField(
            model_name='orderline',
            name='product',
        ),
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderLine',
        ),
    ]
