# Generated by Django 3.0.6 on 2020-05-31 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_auto_20200531_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ans',
            name='next_quest',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='game.Questions'),
        ),
    ]