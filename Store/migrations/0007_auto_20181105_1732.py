# Generated by Django 2.1.2 on 2018-11-05 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0006_itemsout_item_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemsout',
            name='item_user',
            field=models.CharField(max_length=10),
        ),
    ]
