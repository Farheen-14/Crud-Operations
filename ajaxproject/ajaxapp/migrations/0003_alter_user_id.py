# Generated by Django 3.2.7 on 2021-10-03 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ajaxapp', '0002_auto_20210930_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
