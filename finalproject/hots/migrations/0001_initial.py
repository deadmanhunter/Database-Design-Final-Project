# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Abilities',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('default_button', models.CharField(max_length=1)),
                ('ability_name', models.CharField(max_length=200)),
                ('ability_type', models.CharField(max_length=200)),
                ('ability_description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Heroes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hero_name', models.CharField(unique=True, max_length=200)),
                ('base_health', models.IntegerField()),
                ('base_mana', models.IntegerField()),
                ('base_attack', models.IntegerField()),
                ('attack_range', models.IntegerField()),
                ('passive_ability_name', models.CharField(max_length=200)),
                ('passive_ability_description', models.CharField(max_length=255)),
                ('has_alternates', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Ultimate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ultimate_name', models.CharField(max_length=200)),
                ('ultimate_type', models.CharField(max_length=200)),
                ('ultimate_description', models.CharField(max_length=255)),
                ('hero_id', models.ForeignKey(to='hots.Heroes')),
            ],
        ),
        migrations.CreateModel(
            name='Universe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('universe_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='heroes',
            name='home_universe',
            field=models.ForeignKey(to='hots.Universe'),
        ),
        migrations.AddField(
            model_name='abilities',
            name='hero_id',
            field=models.ForeignKey(to='hots.Heroes'),
        ),
    ]
