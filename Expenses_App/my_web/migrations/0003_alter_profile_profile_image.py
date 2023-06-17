# Generated by Django 4.2.2 on 2023-06-17 12:38

import Expenses_App.my_web.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_web', '0002_expense'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='images', validators=[Expenses_App.my_web.validators.validate_image_size]),
        ),
    ]
