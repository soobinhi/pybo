# Generated by Django 3.1.3 on 2022-08-08 00:23

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pybo', '0005_coment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Coment',
            new_name='Comment',
        ),
    ]