# Generated by Django 3.0.6 on 2020-05-13 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('download', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='update_info',
            name='data',
            field=models.ImageField(default=0, upload_to='BinFiles/'),
        ),
    ]
