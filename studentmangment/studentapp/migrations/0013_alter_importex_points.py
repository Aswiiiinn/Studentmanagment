# Generated by Django 5.0.4 on 2024-05-17 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0012_alter_importex_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='importex',
            name='Points',
            field=models.IntegerField(),
        ),
    ]
