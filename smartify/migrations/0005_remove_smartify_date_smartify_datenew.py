# Generated by Django 4.1.7 on 2023-03-14 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartify', '0004_smartify_time_alter_smartify_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='smartify',
            name='date',
        ),
        migrations.AddField(
            model_name='smartify',
            name='dateNew',
            field=models.DateField(blank=True, null=True),
        ),
    ]