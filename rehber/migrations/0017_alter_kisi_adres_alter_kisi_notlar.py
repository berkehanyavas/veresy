# Generated by Django 4.2.5 on 2023-09-13 20:45

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rehber', '0016_remove_kisi_son_islem_remove_kisi_son_miktar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kisi',
            name='adres',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='kisi',
            name='notlar',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
