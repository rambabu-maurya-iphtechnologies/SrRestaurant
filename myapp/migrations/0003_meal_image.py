# Generated by Django 4.0.4 on 2023-06-05 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_meal_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='image',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
    ]
