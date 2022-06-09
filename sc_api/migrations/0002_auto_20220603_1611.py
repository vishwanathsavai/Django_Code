# Generated by Django 3.1.2 on 2022-06-03 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sc_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Random',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField()),
                ('otp', models.IntegerField()),
                ('token', models.CharField(max_length=21)),
                ('pwd', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SportsCenter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('alias', models.CharField(max_length=60)),
            ],
        ),
        migrations.AlterField(
            model_name='hero',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]