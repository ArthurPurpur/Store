# Generated by Django 4.1.7 on 2023-04-04 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cats',
            field=models.ManyToManyField(blank=True, related_name='products', to='store.category'),
        ),
    ]
