# Generated by Django 3.0.5 on 2020-05-06 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0010_activestate_answers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='opentdb_session_key',
            field=models.CharField(default='NONE', max_length=255),
        ),
    ]
