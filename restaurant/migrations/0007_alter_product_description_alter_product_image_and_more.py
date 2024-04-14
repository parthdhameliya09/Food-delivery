# Generated by Django 5.0.2 on 2024-03-15 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0006_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.TextField(max_length=50),
        ),
    ]