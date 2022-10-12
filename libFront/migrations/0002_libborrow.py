# Generated by Django 3.2.9 on 2022-08-07 18:21

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libFront', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='libBorrow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_time', models.DateTimeField()),
                ('p_time', models.DateTimeField()),
                ('f_time', models.DateTimeField(blank=True, default=datetime.datetime(1900, 1, 1, 0, 0), null=True, verbose_name='创建时间')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libFront.libbook')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libFront.libuser')),
            ],
            options={
                'verbose_name': '借书记录',
                'verbose_name_plural': '借书记录',
            },
        ),
    ]
