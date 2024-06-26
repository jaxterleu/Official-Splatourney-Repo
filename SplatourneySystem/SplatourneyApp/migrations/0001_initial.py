# Generated by Django 5.0.3 on 2024-04-03 19:57

import django.db.models.deletion
import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bracket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bracket_ID', models.IntegerField()),
                ('bracket_Name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Moderator',
            fields=[
                ('moderator_username', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('player_ID', models.AutoField(primary_key=True, serialize=False)),
                ('player_in_game_name', models.CharField(blank=True, max_length=20, null=True)),
                ('player_fname', models.CharField(blank=True, max_length=20, null=True)),
                ('player_lname', models.CharField(blank=True, max_length=20, null=True)),
                ('player_dc_id', models.CharField(blank=True, max_length=15, null=True)),
                ('player_fc', models.CharField(blank=True, max_length=14, null=True)),
                ('player_rank', models.CharField(blank=True, max_length=5, null=True)),
                ('player_role', models.CharField(blank=True, max_length=10, null=True)),
                ('player_type', models.CharField(default='member', max_length=10, null=True)),
                ('player_checkin_status', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule_ID', models.IntegerField()),
                ('time_Start', models.TimeField()),
                ('time_End', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_ID', models.IntegerField()),
                ('team_Name', models.CharField(max_length=30)),
                ('wins', models.IntegerField()),
                ('losses', models.IntegerField()),
                ('team_Rank', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('tournament_title', models.CharField(max_length=60, primary_key=True, serialize=False)),
                ('tournament_description', models.CharField(max_length=300)),
                ('tournament_mode', models.CharField(max_length=6)),
                ('registration_status', models.CharField(max_length=18)),
                ('tournament_status', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='BracketColumn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bracketColumn_ID', models.IntegerField()),
                ('bracketColumn_Name', models.CharField(max_length=20)),
                ('bracketColumn_Limit', models.IntegerField()),
                ('bracket_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SplatourneyApp.bracket')),
            ],
        ),
        migrations.CreateModel(
            name='Pairing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pairing_ID', models.IntegerField()),
                ('pairing_Name', models.CharField(max_length=20)),
                ('pairing_Status', models.CharField(max_length=11)),
                ('bracketColumn_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SplatourneyApp.bracketcolumn')),
            ],
        ),
        migrations.CreateModel(
            name='PlayerRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_role', models.CharField(max_length=20)),
                ('player_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SplatourneyApp.player')),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='Team_ID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SplatourneyApp.team'),
        ),
        migrations.CreateModel(
            name='GameEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_Check_in_Status', models.CharField(max_length=11)),
                ('game_Result', models.CharField(max_length=4)),
                ('pairing_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SplatourneyApp.pairing')),
                ('team_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SplatourneyApp.team')),
            ],
        ),
        migrations.AddField(
            model_name='bracket',
            name='tournament_title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SplatourneyApp.tournament'),
        ),
    ]
