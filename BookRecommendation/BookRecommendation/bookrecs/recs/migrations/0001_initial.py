# Generated by Django 2.1.7 on 2019-03-31 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book_list',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Recommended_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rec1', models.IntegerField()),
                ('rec2', models.IntegerField()),
                ('rec3', models.IntegerField()),
                ('rec4', models.IntegerField()),
                ('rec5', models.IntegerField()),
                ('idx', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recs.Book_list')),
            ],
        ),
    ]
