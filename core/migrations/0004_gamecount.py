# Generated by Django 4.2 on 2023-04-25 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_bet_game1_remove_bet_game2_remove_bet_game3_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveSmallIntegerField()),
            ],
        ),
    ]