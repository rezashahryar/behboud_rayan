# Generated by Django 4.2.1 on 2024-03-05 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hamayesh', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hamayesh',
            name='status',
            field=models.CharField(choices=[('in_process', 'درحال اجرا'), ('not_started', 'شروع نشده'), ('end', 'پایان همایش')], default='not_started', max_length=15),
        ),
    ]
