# Generated by Django 3.1 on 2021-04-21 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210420_2014'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='author',
            new_name='author_name',
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(max_length=100),
        ),
    ]
