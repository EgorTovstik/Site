# Generated by Django 4.2.7 on 2023-11-21 14:37

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_article_slug'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='article',
            managers=[
                ('custom', django.db.models.manager.Manager()),
            ],
        ),
    ]
