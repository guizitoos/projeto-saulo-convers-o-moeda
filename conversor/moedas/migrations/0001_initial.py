# Generated by Django 5.1.3 on 2024-11-24 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conversao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('de_moeda', models.CharField(max_length=3)),
                ('para_moeda', models.CharField(max_length=3)),
                ('valor', models.FloatField()),
                ('resultado', models.FloatField()),
                ('data', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
