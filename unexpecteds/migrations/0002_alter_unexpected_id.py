# Generated by Django 4.0.6 on 2022-07-12 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unexpecteds', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unexpected',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
