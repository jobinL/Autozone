# Generated by Django 3.2.25 on 2024-07-11 10:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0016_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='mechanic',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
