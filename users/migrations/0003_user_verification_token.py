# Generated by Django 4.2.3 on 2023-08-07 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_is_email_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='verification_token',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
