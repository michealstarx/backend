# Generated by Django 4.1.7 on 2023-03-14 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartify', '0002_alter_smartify_date_alter_smartify_fimg_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='smartify',
            name='fpara',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='smartify',
            name='outro',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='smartify',
            name='spara',
            field=models.TextField(blank=True, null=True),
        ),
    ]
