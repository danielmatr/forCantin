# Generated by Django 3.2.7 on 2022-04-04 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SuperB', '0002_auto_20220404_0729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='barcode',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, unique=True),
        ),
    ]
