# Generated by Django 4.0.6 on 2022-07-06 01:10

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DistrictModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Tuman')),
                ('sector', models.SmallIntegerField(validators=[django.core.validators.MaxValueValidator(4), django.core.validators.MinValueValidator(1)], verbose_name='Sector')),
            ],
            options={
                'verbose_name': 'Tuman',
                'verbose_name_plural': 'Tumanlar',
            },
        ),
        migrations.CreateModel(
            name='OrganizationNetworkModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Tur')),
            ],
            options={
                'verbose_name': "Tashkilot tarmog'i",
                'verbose_name_plural': "Tashkilot ttarmog'lari",
            },
        ),
        migrations.CreateModel(
            name='RegionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Viloyat')),
            ],
            options={
                'verbose_name': 'Viloyat',
                'verbose_name_plural': 'Viloyatlar',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='TypeOfOrganizationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Tur')),
                ('OrganizationNetwork', models.ManyToManyField(to='organization.organizationnetworkmodel')),
            ],
            options={
                'verbose_name': 'Tashkilot turi',
                'verbose_name_plural': 'Tashkilot turilari',
            },
        ),
        migrations.CreateModel(
            name='OrganizationsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Tashkilot')),
                ('TypeOfOrganization', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='organization.typeoforganizationmodel', verbose_name='type')),
                ('districts', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='organization.districtmodel', verbose_name='districts')),
            ],
            options={
                'verbose_name': 'Tashkilot',
                'verbose_name_plural': 'Tashkilotlar',
            },
        ),
        migrations.AddField(
            model_name='districtmodel',
            name='regions',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='organization.regionmodel', verbose_name='regions'),
        ),
    ]