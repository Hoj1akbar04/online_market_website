# Generated by Django 5.0.3 on 2024-04-20 22:13

import users.helpers
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.ImageField(default=1, upload_to=users.helpers.SaveMediaFile.product_image),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producttypes',
            name='image',
            field=models.ImageField(default=1, upload_to=users.helpers.SaveMediaFile.product_type_image),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producttypes',
            name='price_type',
            field=models.CharField(choices=[('USD', '$'), ('UZS', "SO'M")], default='USD', max_length=8),
        ),
        migrations.AddField(
            model_name='users',
            name='image',
            field=models.ImageField(default=1, upload_to=users.helpers.SaveMediaFile.user_image),
            preserve_default=False,
        ),
    ]
