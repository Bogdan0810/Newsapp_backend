# Generated by Django 2.1.4 on 2019-06-29 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20190629_1731'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='show_articles_first',
            field=models.BooleanField(default=False),
        ),
    ]
