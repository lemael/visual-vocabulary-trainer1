# Generated by Django 3.1 on 2020-08-25 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vocgui', '0004_auto_20200804_1050'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alternativeword',
            old_name='alt_word',
            new_name='word',
        ),
    ]
