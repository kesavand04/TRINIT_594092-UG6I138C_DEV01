# Generated by Django 4.1.6 on 2023-02-11 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngo', '0002_ngodb_ngo_fundingneeds_ngodb_ngo_goal_ngodb_ngo_loc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ngodb',
            name='ngo_goal',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='ngodb',
            name='ngo_name',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='ngodb',
            name='ngo_prevWork',
            field=models.CharField(default='', max_length=500),
        ),
    ]
