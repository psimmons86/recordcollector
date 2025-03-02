# Generated by Django 5.1.6 on 2025-02-14 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_listening'),
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=50)),
                ('website', models.URLField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='listening',
            options={},
        ),
        migrations.AddField(
            model_name='record',
            name='labels',
            field=models.ManyToManyField(to='main_app.label'),
        ),
    ]
