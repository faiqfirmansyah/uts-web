# Generated by Django 5.0.6 on 2024-05-11 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Barang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('deskripsi', models.TextField()),
                ('jumlah', models.IntegerField(default=0)),
                ('tanggal_masuk', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
