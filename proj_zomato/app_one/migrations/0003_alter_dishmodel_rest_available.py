# Generated by Django 3.2.9 on 2021-11-10 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_one', '0002_alter_usermodel_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dishmodel',
            name='rest_available',
            field=models.CharField(max_length=500),
        ),
    ]