# Generated by Django 3.2.5 on 2022-01-25 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BlogPost',
            new_name='Profile',
        ),
    ]
