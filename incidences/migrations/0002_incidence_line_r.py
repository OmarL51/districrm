# Generated by Django 2.1.15 on 2022-07-06 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incidences', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='incidence',
            name='line_r',
            field=models.IntegerField(default=0),
        ),
    ]