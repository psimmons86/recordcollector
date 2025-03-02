# Generated by Django 5.1.6 on 2025-02-12 21:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_add_new_records'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listening',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Listening date')),
                ('time', models.CharField(choices=[('M', 'Morning'), ('A', 'Afternoon'), ('E', 'Evening'), ('N', 'Night')], default='M', max_length=1)),
                ('record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.record')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
