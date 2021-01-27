# Generated by Django 3.1.5 on 2021-01-27 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('image', models.ImageField(upload_to='pictures/')),
                ('size', models.CharField(max_length=30)),
                ('style', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=30)),
            ],
        ),
    ]
