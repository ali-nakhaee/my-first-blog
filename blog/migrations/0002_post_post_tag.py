# Generated by Django 3.2.23 on 2023-12-28 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_tag',
            field=models.CharField(default='main', max_length=50),
        ),
    ]
