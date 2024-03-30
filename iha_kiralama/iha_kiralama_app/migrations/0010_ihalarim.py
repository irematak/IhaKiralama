# Generated by Django 5.0.3 on 2024-03-29 18:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iha_kiralama_app', '0009_iha_havada_kalıs_suresi_alter_iha_uzunluk'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ihalarim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marka', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('agirlik', models.FloatField()),
                ('uzunluk', models.FloatField()),
                ('havada_kalıs_suresi', models.FloatField()),
                ('olusturan_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]