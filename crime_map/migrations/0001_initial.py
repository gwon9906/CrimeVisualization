# Generated by Django 5.0.6 on 2024-06-08 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CrimeData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station', models.CharField(max_length=100)),
                ('crime_type', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('murder', models.IntegerField(default=0)),
                ('robbery', models.IntegerField(default=0)),
                ('sexual_crime', models.IntegerField(default=0)),
                ('theft', models.IntegerField(default=0)),
                ('violence', models.IntegerField(default=0)),
            ],
        ),
    ]