# Generated by Django 5.0.3 on 2024-03-27 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iha_kiralama_app', '0005_kiralananiha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kiralananiha',
            name='user_id',
            field=models.IntegerField(),
        ),
    ]
