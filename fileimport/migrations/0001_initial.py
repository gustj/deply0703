# Generated by Django 2.2.1 on 2019-05-30 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ewhaclass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseno', models.CharField(max_length=10)),
                ('classno', models.CharField(max_length=5)),
                ('title', models.CharField(max_length=50)),
                ('classification', models.CharField(max_length=50)),
                ('instructor', models.CharField(max_length=50)),
                ('credit', models.CharField(max_length=50)),
                ('hourt', models.CharField(max_length=50)),
            ],
        ),
    ]
