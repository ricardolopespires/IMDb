# Generated by Django 3.1 on 2021-02-26 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('serie', '0001_initial'),
        ('movie', '0001_initial'),
        ('documentary', '0001_initial'),
        ('actor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='documentarys',
            field=models.ManyToManyField(to='documentary.Documentary'),
        ),
        migrations.AddField(
            model_name='actor',
            name='movies',
            field=models.ManyToManyField(to='movie.Movie'),
        ),
        migrations.AddField(
            model_name='actor',
            name='series',
            field=models.ManyToManyField(to='serie.Serie'),
        ),
    ]
