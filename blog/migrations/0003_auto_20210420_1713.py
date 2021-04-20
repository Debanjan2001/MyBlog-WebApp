# Generated by Django 3.1 on 2021-04-20 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_comment_approved_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='preview_img_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='short_text',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
