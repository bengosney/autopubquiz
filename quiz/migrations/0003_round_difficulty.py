# Generated by Django 3.0.5 on 2020-04-28 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20200428_0713'),
    ]

    operations = [
        migrations.AddField(
            model_name='round',
            name='difficulty',
            field=models.CharField(choices=[(None, 'Any'), ('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')], default=None, max_length=255),
        ),
    ]
