# Generated by Django 3.1.4 on 2020-12-06 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(blank=True, max_length=250, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]