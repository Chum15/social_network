# Generated by Django 5.1.5 on 2025-02-11 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0015_alter_like_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='like',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='post',
            unique_together=set(),
        ),
    ]
