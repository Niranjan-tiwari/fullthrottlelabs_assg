# Generated by Django 3.1.1 on 2020-09-26 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activity_api', '0005_auto_20200926_1854'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='memberactivity',
            name='member',
        ),
        migrations.AddField(
            model_name='member',
            name='member_activity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='member_activity', to='activity_api.memberactivity'),
        ),
    ]
