# Generated by Django 2.0.6 on 2018-08-05 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0002_auto_20180802_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='content',
            field=models.TextField(help_text='Content of the Note', max_length=512, verbose_name='Content'),
        ),
    ]