# Generated by Django 3.0.3 on 2020-02-11 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0008_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
