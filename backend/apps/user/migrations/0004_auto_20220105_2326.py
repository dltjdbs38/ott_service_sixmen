# Generated by Django 3.2.6 on 2022-01-05 23:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20220105_1821'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preferottcontentgenre',
            name='user',
        ),
        migrations.AddField(
            model_name='user',
            name='prefer_ott_content_genre',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.preferottcontentgenre'),
        ),
    ]
