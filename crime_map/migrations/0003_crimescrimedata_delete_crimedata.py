# Generated by Django 5.0.6 on 2024-06-09 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crime_map', '0002_remove_crimedata_crime_type_alter_crimedata_murder_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CrimesCrimedata',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('station', models.CharField(max_length=100)),
                ('crime_type', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('murder', models.IntegerField()),
                ('robbery', models.IntegerField()),
                ('sexual_crime', models.IntegerField()),
                ('theft', models.IntegerField()),
                ('violence', models.IntegerField()),
            ],
            options={
                'db_table': 'crimes_crimedata',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='CrimeData',
        ),
    ]
