# Generated by Django 3.0.5 on 2020-04-20 12:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('game', '0002_auto_20200418_1339'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.png', upload_to='profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='gamesession',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='game.Profile'),
        ),
        migrations.AlterField(
            model_name='playeralias',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='game.Profile'),
        ),
    ]
