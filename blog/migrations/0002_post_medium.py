# Generated by Django 2.0.2 on 2018-07-16 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='medium',
            field=models.URLField(blank=True, max_length=250, null=True),
        ),
    ]
