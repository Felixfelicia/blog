# Generated by Django 4.2.2 on 2023-06-13 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_hashtag'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Hashtag',
            new_name='Category',
        ),
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(to='products.category'),
        ),
    ]
