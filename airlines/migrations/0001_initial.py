# Generated by Django 2.0.6 on 2018-06-29 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airliner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=8)),
                ('title', models.CharField(max_length=32)),
            ],
            options={
                'verbose_name': 'Авиалайнер',
                'verbose_name_plural': 'Авиалайнеры',
            },
        ),
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=8)),
                ('title', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name': 'Аэропорт',
                'verbose_name_plural': 'Аэропорты',
            },
        ),
        migrations.CreateModel(
            name='DayOfWeek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=16)),
            ],
            options={
                'verbose_name': 'День недели',
                'verbose_name_plural': 'Дни недели',
            },
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField()),
                ('arrival', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrivals', to='airlines.Airport')),
                ('departure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departures', to='airlines.Airport')),
            ],
            options={
                'verbose_name': 'Перелет',
                'verbose_name_plural': 'Перелеты',
            },
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=8)),
            ],
            options={
                'verbose_name': 'Маршрут',
                'verbose_name_plural': 'Маршруты',
            },
        ),
        migrations.CreateModel(
            name='ScheduleRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('per_day', models.IntegerField()),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='airlines.DayOfWeek')),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='airlines.Route')),
            ],
            options={
                'verbose_name': 'Записи расписания',
                'verbose_name_plural': 'Записи расписания',
            },
        ),
        migrations.AddField(
            model_name='route',
            name='schedule',
            field=models.ManyToManyField(through='airlines.ScheduleRecord', to='airlines.DayOfWeek'),
        ),
        migrations.AddField(
            model_name='flight',
            name='route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='airlines.Route'),
        ),
        migrations.AddField(
            model_name='airliner',
            name='routes',
            field=models.ManyToManyField(to='airlines.Route'),
        ),
    ]