# Generated by Django 3.2.7 on 2021-10-06 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(default='', max_length=100)),
                ('last', models.CharField(default='', max_length=100)),
                ('vip', models.IntegerField(default=-1)),
                ('email', models.CharField(default='', max_length=100)),
            ],
        ),
    ]