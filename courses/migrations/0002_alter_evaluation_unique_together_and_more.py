# Generated by Django 4.0 on 2021-12-16 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='evaluation',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='evaluation',
            name='course',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Evaluation',
        ),
    ]
