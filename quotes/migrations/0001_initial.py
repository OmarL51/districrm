# Generated by Django 4.0.4 on 2022-05-24 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('means', '0001_initial'),
        ('thirds', '0003_third_contacto_third_correo_third_direccion_and_more'),
        ('statuses', '0003_status_color_s'),
        ('unexpecteds', '0003_unexpected_color_u'),
        ('zones', '0001_initial'),
        ('incidencetypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_cot', models.DateTimeField(blank=True, null=True)),
                ('incidencety2', models.CharField(max_length=100)),
                ('tittle_cot', models.CharField(max_length=100)),
                ('num_cot', models.IntegerField()),
                ('line', models.IntegerField(default=0)),
                ('assign', models.CharField(max_length=100)),
                ('recotization', models.BooleanField()),
                ('date_ppta', models.DateTimeField(blank=True, null=True)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('observation', models.CharField(max_length=500)),
                ('incidencety', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='incidencetypes.incidencety')),
                ('mean', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='means.mean')),
                ('status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='statuses.status')),
                ('third', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='thirds.third')),
                ('unexpected', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='unexpecteds.unexpected')),
                ('zone', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='zones.zone')),
            ],
        ),
    ]
