# Generated by Django 3.2.5 on 2022-01-27 05:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0011_profile_cv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skillset',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='profiles.profile'),
        ),
    ]
