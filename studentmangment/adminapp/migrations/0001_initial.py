# Generated by Django 5.0.4 on 2024-06-07 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='announcment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Headings', models.CharField(max_length=25)),
                ('announcement_details', models.TextField(max_length=255)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('expire_date', models.DateField()),
            ],
        ),
    ]
