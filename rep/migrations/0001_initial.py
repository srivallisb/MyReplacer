# Generated by Django 3.0.3 on 2020-03-23 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='String',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('paragraph', models.TextField(blank=True, null=True)),
                ('substring_to_be_replaced', models.CharField(blank=True, max_length=100, null=True)),
                ('replace_word', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
