# Generated by Django 4.1.1 on 2022-12-30 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeproduct',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
