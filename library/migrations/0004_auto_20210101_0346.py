# Generated by Django 3.1.4 on 2020-12-31 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_auto_20201231_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(null=True, upload_to='images/cover'),
        ),
    ]
