# Generated by Django 4.1.1 on 2022-12-27 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_homeproduct_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeproduct',
            name='image',
            field=models.ImageField(default='', upload_to='media'),
        ),
    ]
