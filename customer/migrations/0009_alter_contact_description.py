# Generated by Django 5.0.2 on 2024-03-18 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0008_alter_contact_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='description',
            field=models.TextField(max_length=200),
        ),
    ]