# Generated by Django 4.2.5 on 2023-09-09 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rehber', '0008_kisi_son_miktar_alter_kisi_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kisi',
            name='son_islem',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='kisi',
            name='son_miktar',
            field=models.FloatField(blank=True),
        ),
    ]
