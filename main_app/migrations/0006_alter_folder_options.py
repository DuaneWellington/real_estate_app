# Generated by Django 5.0.1 on 2024-01-20 02:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_rename_user_property_user_rename_user_rental_user_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='folder',
            options={'permissions': [('can_add_folder', 'Add Folder'), ('can_delete_folder', 'Delete Folder'), ('can_edit_folder', 'Edit Folder'), ('can_view_folder', 'View Folder')]},
        ),
    ]
