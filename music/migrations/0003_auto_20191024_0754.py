# Generated by Django 2.2.1 on 2019-10-24 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20191024_0751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='playlist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='albums', to='music.Playlist'),
        ),
        migrations.AlterField(
            model_name='song',
            name='album',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='music.Album'),
        ),
        migrations.AlterField(
            model_name='song',
            name='playlist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='songs', to='music.Playlist'),
        ),
    ]
