# Generated by Django 4.2.2 on 2023-06-22 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_alter_menu_inventory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='inventory',
        ),
        migrations.AddField(
            model_name='menuitem',
            name='inventory',
            field=models.PositiveIntegerField(default=100),
        ),
    ]