# Generated by Django 2.2.24 on 2021-08-07 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyBlog_blog', '0002_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='has_consented',
            field=models.BooleanField(null=True, verbose_name='Secim'),
        ),
    ]
