# Generated by Django 4.2.1 on 2024-03-08 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hamayesh', '0004_alter_hamayesh_date_of_hamayesh'),
    ]

    operations = [
        migrations.AddField(
            model_name='hamayesh',
            name='image',
            field=models.ImageField(null=True, upload_to='hamayeshat/'),
        ),
    ]
