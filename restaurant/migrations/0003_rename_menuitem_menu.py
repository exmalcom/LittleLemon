# Generated by Django 4.2.16 on 2024-11-10 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_rename_menu_menuitem'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MenuItem',
            new_name='Menu',
        ),
    ]
