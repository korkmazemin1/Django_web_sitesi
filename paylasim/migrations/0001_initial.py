# Generated by Django 4.1.4 on 2022-12-19 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='kullanici',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=255)),
                ('soyisim', models.CharField(max_length=255)),
            ],
        ),
    ]