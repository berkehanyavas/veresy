# Generated by Django 4.2.1 on 2023-09-13 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rehber', '0013_remove_kisi_grup_delete_grup'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kisi',
            name='total',
        ),
    ]
