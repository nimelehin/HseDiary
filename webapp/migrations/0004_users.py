# Generated by Django 2.0.6 on 2018-06-03 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20180602_1525'),
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yandexUserId', models.CharField(default='none', max_length=300)),
                ('eljurUserId', models.CharField(default='none', max_length=300)),
            ],
        ),
    ]
