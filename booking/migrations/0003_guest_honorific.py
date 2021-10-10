# Generated by Django 3.2.7 on 2021-10-06 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_guest'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='honorific',
            field=models.CharField(choices=[('MR', 'Mr.'), ('MS', 'Ms.'), ('DR', 'Dr.'), ('OT', 'Other')], default='OT', max_length=2),
        ),
    ]
