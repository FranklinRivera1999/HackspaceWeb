# Generated by Django 3.0.2 on 2020-01-15 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('correo', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('consult', models.CharField(max_length=1000)),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.User')),
            ],
        ),
        migrations.CreateModel(
            name='Commentary',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.CharField(max_length=250)),
                ('postid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.Post')),
            ],
        ),
    ]
