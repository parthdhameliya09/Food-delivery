# Generated by Django 5.0.2 on 2024-03-18 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0010_store_delete_category_delete_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='store',
            old_name='staddress',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='store',
            old_name='stmobile',
            new_name='mobile',
        ),
        migrations.RenameField(
            model_name='store',
            old_name='stname',
            new_name='name',
        ),
    ]
