# Generated by Django 4.1.6 on 2023-02-11 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngo', '0003_alter_ngodb_ngo_goal_alter_ngodb_ngo_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ngodb',
            name='ngo_fundingNeeds',
        ),
        migrations.AddField(
            model_name='ngodb',
            name='ngo_pass',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='ngodb',
            name='ngo_phoneNo',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='phildb',
            name='phil_pass',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='ngodb',
            name='ngo_sector',
            field=models.CharField(default='', max_length=100),
        ),
    ]