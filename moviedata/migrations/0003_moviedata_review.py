# Generated by Django 3.1.3 on 2020-11-08 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviedata', '0002_auto_20201108_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedata',
            name='review',
            field=models.TextField(blank=True, max_length=1000),
        ),
    ]
