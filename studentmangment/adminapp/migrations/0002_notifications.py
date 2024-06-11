# Generated by Django 5.0.4 on 2024-06-07 08:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0001_initial'),
        ('studentapp', '0021_attandence1'),
    ]

    operations = [
        migrations.CreateModel(
            name='notifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('notification_details', models.TextField(max_length=255)),
                ('document', models.FileField(blank=True, null=True, upload_to='notification/')),
                ('posted_date', models.DateField()),
                ('expire_date', models.DateField()),
                ('teacher_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='studentapp.teacher')),
            ],
        ),
    ]
