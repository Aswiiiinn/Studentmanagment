# Generated by Django 5.0.4 on 2024-05-17 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0016_alter_importex_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='importex',
            name='Points',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
    ]
