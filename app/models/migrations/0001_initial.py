# Generated by Django 3.0.4 on 2020-03-29 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelMetadata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SlugField(max_length=60)),
                ('description', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ModelParameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('type', models.CharField(choices=[('NUMBER', 'Number'), ('STRING', 'String')], max_length=10)),
                ('description', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
