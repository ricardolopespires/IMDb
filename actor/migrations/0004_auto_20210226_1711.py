# Generated by Django 3.1 on 2021-02-26 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_auto_20210226_1708'),
        ('serie', '0006_auto_20210226_1512'),
        ('documentary', '0002_auto_20210226_1021'),
        ('actor', '0003_auto_20210226_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='documentarys',
            field=models.ManyToManyField(blank=True, to='documentary.Documentary'),
        ),
        migrations.AlterField(
            model_name='actor',
            name='movies',
            field=models.ManyToManyField(blank=True, to='movie.Movie'),
        ),
        migrations.AlterField(
            model_name='actor',
            name='series',
            field=models.ManyToManyField(blank=True, to='serie.Serie'),
        ),
    ]