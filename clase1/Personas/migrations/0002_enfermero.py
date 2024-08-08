# Generated by Django 5.0.7 on 2024-07-23 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Personas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enfermero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rfc', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('turno', models.CharField(max_length=50)),
                ('hospital', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
