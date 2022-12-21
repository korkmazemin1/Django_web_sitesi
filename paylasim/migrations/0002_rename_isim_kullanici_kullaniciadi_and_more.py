# Generated by Django 4.1.4 on 2022-12-19 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paylasim', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kullanici',
            old_name='isim',
            new_name='kullaniciadi',
        ),
        migrations.RemoveField(
            model_name='kullanici',
            name='soyisim',
        ),
        migrations.AddField(
            model_name='kullanici',
            name='foto',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]