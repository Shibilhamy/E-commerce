# Generated by Django 5.0.1 on 2024-01-15 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AvailableOffers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('off_head', models.CharField(max_length=200)),
                ('off_des', models.CharField(max_length=500)),
            ],
        ),
    ]