# Generated by Django 3.1.1 on 2020-09-26 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activity_api', '0003_auto_20200926_1811'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='activity_periods',
        ),
        migrations.AddField(
            model_name='memberactivity',
            name='member',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='activity_api.member'),
        ),
    ]
