# Generated by Django 3.1.2 on 2022-06-03 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sc_api', '0003_auto_20220603_1653'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='fname',
            new_name='c_rl_nm',
        ),
        migrations.RemoveField(
            model_name='student',
            name='lname',
        ),
        migrations.RemoveField(
            model_name='student',
            name='roll',
        ),
        migrations.RemoveField(
            model_name='student',
            name='sclass',
        ),
        migrations.AlterModelTable(
            name='student',
            table='role',
        ),
    ]
