# Generated by Django 4.0.6 on 2022-07-06 01:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_typeoforganizationmodel_organizationnetworkmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizationsmodel',
            name='OrganizationNetworkModel',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='organization.organizationnetworkmodel', verbose_name='tarmog'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organizationsmodel',
            name='TypeOfOrganization',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.PROTECT, to='organization.typeoforganizationmodel', verbose_name='turi'),
            preserve_default=False,
        ),
    ]
