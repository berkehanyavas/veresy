# Generated by Django 4.2.5 on 2023-09-08 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rehber', '0002_kisi_tel1_kisi_tel2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kisi',
            name='adres',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='kisi',
            name='notlar',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='kisi',
            name='tel1',
            field=models.CharField(blank=True, max_length=444, null=True),
        ),
        migrations.AlterField(
            model_name='kisi',
            name='tel2',
            field=models.CharField(blank=True, max_length=444, null=True),
        ),
    ]
