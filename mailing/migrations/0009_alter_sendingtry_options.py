# Generated by Django 4.2.4 on 2023-08-28 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0008_remove_mailingsetting_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sendingtry',
            options={'verbose_name': 'Попытка рассылки', 'verbose_name_plural': 'Попытки рассылки'},
        ),
    ]