# Generated by Django 2.2.20 on 2021-05-18 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='propiedades',
            name='foto',
            field=models.ImageField(default=2, upload_to='', verbose_name='imagen de propiedad'),
            preserve_default=False,
        ),
    ]
