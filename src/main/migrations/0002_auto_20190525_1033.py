# Generated by Django 2.2.1 on 2019-05-25 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='field',
            options={'verbose_name': 'Pista', 'verbose_name_plural': 'Pistes'},
        ),
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name': 'Grup'},
        ),
        migrations.AlterModelOptions(
            name='match',
            options={'ordering': ['start_time', 'game_field'], 'verbose_name': 'Partit'},
        ),
        migrations.AlterField(
            model_name='match',
            name='start_time',
            field=models.DateTimeField(verbose_name='Hora de joc'),
        ),
    ]