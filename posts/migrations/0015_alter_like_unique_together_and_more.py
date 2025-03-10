# Generated by Django 5.1.5 on 2025-02-11 10:31

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0014_like_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='like',
            unique_together={('user', 'post')},
        ),
        migrations.AlterUniqueTogether(
            name='post',
            unique_together={('author', 'text')},
        ),
    ]
