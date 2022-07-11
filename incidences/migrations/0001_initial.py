# Generated by Django 2.1.15 on 2022-07-06 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('incidencetypes', '0001_initial'),
        ('means', '0001_initial'),
        ('statuses', '0001_initial'),
        ('thirds', '0001_initial'),
        ('unexpecteds', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Incidence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_oc', models.DateTimeField(blank=True, null=True)),
                ('tittle', models.CharField(max_length=100)),
                ('oc_client', models.CharField(max_length=100)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('assign', models.CharField(max_length=100)),
                ('order', models.IntegerField()),
                ('line', models.IntegerField(default=0)),
                ('rmv', models.IntegerField()),
                ('date_rmv', models.DateTimeField(blank=True, null=True)),
                ('incidencety', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='incidencetypes.Incidencety')),
                ('mean', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='means.Mean')),
                ('status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='statuses.Status')),
                ('third', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='thirds.Third')),
                ('unexpected', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='unexpecteds.Unexpected')),
            ],
        ),
    ]
