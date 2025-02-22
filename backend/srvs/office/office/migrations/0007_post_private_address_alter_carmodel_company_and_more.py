# Generated by Django 5.1.4 on 2024-12-24 11:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0006_post_latitude_post_longitude'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='private_address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='car_models', to='office.company'),
        ),
        migrations.AlterField(
            model_name='post',
            name='car_model',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='office.carmodel'),
        ),
        migrations.AlterField(
            model_name='post',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='office.company'),
        ),
    ]
