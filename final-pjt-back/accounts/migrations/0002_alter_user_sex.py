# Generated by Django 3.2.13 on 2022-11-17 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(choices=[('female', 'Female'), ('male', 'Male')], default='male', max_length=10),
        ),
    ]
