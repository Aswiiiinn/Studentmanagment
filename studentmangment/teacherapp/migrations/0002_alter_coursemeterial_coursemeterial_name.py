# Generated by Django 5.0.4 on 2024-05-16 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacherapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursemeterial',
            name='coursemeterial_name',
            field=models.CharField(blank=True, default=None, max_length=45, null=True),
        ),
    ]