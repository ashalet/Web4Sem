# Generated by Django 4.1.2 on 2022-11-01 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_alter_assets_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assets',
            name='image',
            field=models.ImageField(unique=True, upload_to='static/portfolio/img/'),
        ),
    ]
