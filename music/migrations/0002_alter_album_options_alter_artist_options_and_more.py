# Generated by Django 5.0.3 on 2024-05-12 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='artist',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='song',
            options={'ordering': ['id']},
        ),
        migrations.AddField(
            model_name='album',
            name='watching',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='song',
            name='listened',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AddIndex(
            model_name='album',
            index=models.Index(fields=['id'], name='music_album_id_a66d97_idx'),
        ),
        migrations.AddIndex(
            model_name='artist',
            index=models.Index(fields=['id'], name='music_artis_id_a6462a_idx'),
        ),
        migrations.AddIndex(
            model_name='song',
            index=models.Index(fields=['id'], name='music_song_id_82e124_idx'),
        ),
    ]
