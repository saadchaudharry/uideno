# Generated by Django 2.2.7 on 2020-05-25 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maincat', '0003_prod_publish'),
    ]

    operations = [
        migrations.AddField(
            model_name='catagory',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True),
        ),
    ]
