# Generated by Django 4.2.5 on 2023-09-13 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rehber', '0015_alter_kisi_son_islem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kisi',
            name='son_islem',
        ),
        migrations.RemoveField(
            model_name='kisi',
            name='son_miktar',
        ),
    ]
