from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_post_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_tag',
            field=models.CharField(default='', max_length=50),
        ),
    ]
