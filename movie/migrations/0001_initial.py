# Generated by Django 3.1 on 2021-02-26 13:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('actor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200)),
                ('Year', models.CharField(blank=True, max_length=25)),
                ('Publish', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
                ('Status', models.CharField(blank=True, choices=[('cartaz', 'Cartaz'), ('em breve', 'Em Breve'), ('lançamento', 'Lançamento'), ('geral', 'Geral'), ('novo', 'Novo')], default='geral', max_length=140)),
                ('Popularity', models.IntegerField()),
                ('Rated', models.CharField(blank=True, max_length=10)),
                ('Released', models.CharField(blank=True, max_length=25)),
                ('Runtime', models.CharField(blank=True, max_length=25)),
                ('Director', models.CharField(blank=True, max_length=100)),
                ('Writer', models.CharField(blank=True, max_length=300)),
                ('Plot', models.CharField(blank=True, max_length=900)),
                ('Language', models.CharField(blank=True, max_length=300)),
                ('Country', models.CharField(blank=True, max_length=100)),
                ('Awards', models.CharField(blank=True, max_length=250)),
                ('Poster', models.ImageField(blank=True, upload_to='movies')),
                ('Poster_url', models.URLField(blank=True)),
                ('Metascore', models.CharField(blank=True, max_length=5)),
                ('imdbRating', models.CharField(blank=True, max_length=5)),
                ('imdbCount', models.CharField(blank=True, max_length=100)),
                ('imdbVotes', models.CharField(blank=True, max_length=100)),
                ('imdbID', models.CharField(blank=True, max_length=100)),
                ('Filmes_views', models.IntegerField(blank=True, default=0)),
                ('Video', models.IntegerField(blank=True, default=0)),
                ('Trailer', models.CharField(blank=True, max_length=100)),
                ('Watched', models.IntegerField(blank=True, default=0)),
                ('Type', models.CharField(blank=True, max_length=10)),
                ('DVD', models.CharField(blank=True, max_length=25)),
                ('BoxOffice', models.CharField(blank=True, max_length=25)),
                ('Production', models.CharField(blank=True, max_length=100)),
                ('Website', models.CharField(blank=True, max_length=150)),
                ('totalSeasons', models.CharField(blank=True, max_length=3)),
                ('Actors', models.ManyToManyField(blank=True, to='actor.Actor')),
                ('Genre', models.ManyToManyField(blank=True, to='movie.Genre')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=50)),
                ('rating', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField(blank=True, max_length=3000)),
                ('rate', models.PositiveSmallIntegerField(choices=[(1, '1 - Trash'), (2, '2 - Horrible'), (3, '3 - Terrible'), (4, '4 - Bad'), (5, '5 - OK'), (6, '6 - Watchable'), (7, '7 - Good'), (8, '8 - Very Good'), (9, '9 - Perfect'), (10, '10 - Master Piece')])),
                ('likes', models.PositiveIntegerField(default=0)),
                ('unlikes', models.PositiveIntegerField(default=0)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='Ratings',
            field=models.ManyToManyField(blank=True, to='movie.Rating'),
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_like', models.PositiveSmallIntegerField()),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_like', to='movie.review')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_like', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
