# Generated by Django 3.1.5 on 2021-01-27 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picture_types', '0001_initial'),
        ('pictures', '0002_auto_20210127_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='types',
            field=models.ManyToManyField(related_name='pictures', to='picture_types.PictureType'),
        ),
    ]
