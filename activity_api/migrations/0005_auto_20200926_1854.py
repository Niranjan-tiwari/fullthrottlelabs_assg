# Generated by Django 3.1.1 on 2020-09-26 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activity_api', '0004_auto_20200926_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberactivity',
            name='member',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='member_activity', to='activity_api.member'),
        ),
    ]
