# Generated by Django 3.1.12 on 2022-12-23 13:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('files', '0003_auto_20210927_1245'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='members',
            field=models.ManyToManyField(blank=True, help_text='Members of the category have access to the media.', related_name='accessible_categories', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='media',
            name='allow_download',
            field=models.BooleanField(default=False, help_text='Whether option to download media is shown'),
        ),
        migrations.AlterField(
            model_name='media',
            name='is_reviewed',
            field=models.BooleanField(db_index=True, default=False, help_text='Whether media is reviewed, so it can appear on public listings'),
        ),
        migrations.AlterField(
            model_name='media',
            name='state',
            field=models.CharField(choices=[('private', 'Private'), ('protected', 'Protected'), ('public', 'Public'), ('unlisted', 'Unlisted')], db_index=True, default='private', help_text='state of Media', max_length=20),
        ),
    ]