# Generated by Django 3.2.8 on 2022-03-04 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0003_project_vote_ratio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cladire',
            fields=[
                ('codCladire', models.AutoField(primary_key=True, serialize=False)),
                ('denCladire', models.CharField(max_length=30)),
                ('adresaCladire', models.CharField(max_length=200)),
                ('nrEtaje', models.IntegerField()),
            ],
        ),
    ]
