# Generated by Django 5.1.4 on 2025-01-15 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gate', '0003_user_password_updated_at_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.EmailField(max_length=255, unique=True),
        ),
    ]
