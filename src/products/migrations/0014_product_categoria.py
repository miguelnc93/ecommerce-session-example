# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-08-21 02:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='categoria',
            field=models.CharField(blank=True, choices=[('MUJER', 'MUJER'), ('HOMBRE', 'HOMBRE'), ('MERCADO', 'MERCADO')], max_length=20, null=True),
        ),
    ]
