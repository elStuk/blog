# Generated by Django 2.2 on 2019-05-03 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20190503_1031'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post_lkes',
            new_name='post_likes',
        ),
    ]
