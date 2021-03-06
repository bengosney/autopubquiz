# Generated by Django 3.0.5 on 2020-04-30 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_auto_20200430_0746'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['position']},
        ),
        migrations.AlterModelOptions(
            name='round',
            options={'ordering': ['position']},
        ),
        migrations.AlterField(
            model_name='question',
            name='position',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='round',
            name='position',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
