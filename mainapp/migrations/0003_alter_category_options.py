# Generated by Django 4.0.4 on 2022-06-03 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('pk',), 'verbose_name': 'категория', 'verbose_name_plural': 'категории'},
        ),
    ]
