# Generated by Django 2.1.5 on 2019-02-11 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='commentreply',
            options={'ordering': ['-created_at']},
        ),
    ]
