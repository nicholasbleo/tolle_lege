# Generated by Django 4.2.4 on 2023-12-09 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reader', '0005_alter_morpheme_page_index'),
    ]

    operations = [
        migrations.AlterField(
            model_name='morpheme',
            name='parse',
            field=models.TextField(verbose_name='parse'),
        ),
    ]
