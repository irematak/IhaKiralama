# Generated by Django 5.0.3 on 2024-03-29 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iha_kiralama_app', '0010_ihalarim'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ihalarim',
            old_name='olusturan_id',
            new_name='olusturan',
        ),
    ]