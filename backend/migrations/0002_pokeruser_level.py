# Generated by Django 2.1.4 on 2019-04-12 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokeruser',
            name='level',
            field=models.CharField(choices=[('BG', 'Begginer'), ('AD', 'Advanced'), ('IM', 'Intermediate')], default='BG', max_length=2),
        ),
    ]
