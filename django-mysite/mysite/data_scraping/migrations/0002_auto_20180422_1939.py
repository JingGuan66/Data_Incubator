# Generated by Django 2.0.4 on 2018-04-22 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_scraping', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
