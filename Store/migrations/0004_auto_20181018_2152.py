# Generated by Django 2.1.2 on 2018-10-18 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0003_remove_itemsin_order_num'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Items_out',
            new_name='ItemsOut',
        ),
    ]