# Generated by Django 5.0.6 on 2024-06-14 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocgui', '0006_auto_20200825_1216'),
    ]

    operations = [
        migrations.CreateModel(
            name='PdfFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.FileField(upload_to='pdfFile/')),
            ],
        ),
    ]
