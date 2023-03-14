# Generated by Django 4.1.7 on 2023-03-13 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartify', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smartify',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='smartify',
            name='fimg',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='smartify',
            name='intro',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='smartify',
            name='oimg',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='smartify',
            name='simg',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='smartify',
            name='timg',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='smartify',
            name='title',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]