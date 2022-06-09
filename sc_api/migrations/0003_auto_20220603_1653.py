# Generated by Django 3.1.2 on 2022-06-03 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sc_api', '0002_auto_20220603_1611'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll', models.CharField(max_length=100)),
                ('sclass', models.CharField(max_length=100)),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.DeleteModel(
            name='Hero',
        ),
        migrations.DeleteModel(
            name='Random',
        ),
        migrations.DeleteModel(
            name='SportsCenter',
        ),
    ]