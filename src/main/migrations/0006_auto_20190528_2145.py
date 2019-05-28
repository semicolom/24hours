# Generated by Django 2.2.1 on 2019-05-28 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20190526_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='modality',
            field=models.CharField(choices=[('masc', 'Masculí'), ('fem', 'Femení'), ('mix', 'Mixt')], max_length=255, verbose_name='Modalitat'),
        ),
        migrations.AlterField(
            model_name='team',
            name='modality',
            field=models.CharField(choices=[('masc', 'Masculí'), ('fem', 'Femení'), ('mix', 'Mixt')], max_length=255, verbose_name='Modalitat'),
        ),
    ]