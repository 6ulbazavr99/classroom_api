# Generated by Django 5.0 on 2023-12-12 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='description',
            field=models.TextField(),
        ),
    ]
