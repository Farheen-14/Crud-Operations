# Generated by Django 3.1.3 on 2021-09-30 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ajaxapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]