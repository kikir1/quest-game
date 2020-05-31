# Generated by Django 3.0.6 on 2020-05-30 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(db_index=True, max_length=150)),
                ('nq', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='game.Questions')),
                ('quest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.Questions')),
            ],
        ),
    ]