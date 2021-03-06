# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-28 00:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Investor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wallet', models.CharField(max_length=100, verbose_name='Wallet')),
                ('passport', models.ImageField(upload_to='')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('investor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='startup.Investor')),
            ],
        ),
        migrations.CreateModel(
            name='Startup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Startup name')),
                ('description', models.TextField(verbose_name='Description')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='')),
                ('goal', models.IntegerField(verbose_name='Goal')),
                ('vip', models.BooleanField(default=False)),
                ('wallet', models.CharField(max_length=100, verbose_name='Wallet')),
                ('website', models.CharField(max_length=100, verbose_name='Website')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('launch_date', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='startup',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='startup.Startup'),
        ),
    ]
