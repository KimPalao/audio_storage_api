# Generated by Django 4.2.3 on 2023-07-28 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_audio_file_audiofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiofile',
            name='audio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='api.audio'),
        ),
        migrations.AlterField(
            model_name='audiofile',
            name='notes',
            field=models.TextField(blank=True),
        ),
    ]
