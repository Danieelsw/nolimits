# Generated by Django 4.2 on 2023-05-24 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nolimits', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='imagen_bd/'),
        ),
    ]
