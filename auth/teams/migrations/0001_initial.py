# Generated by Django 4.2.5 on 2023-09-19 20:25

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('teamName', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, default='/images/placeholder.png', null=True, upload_to='images/')),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'permissions': [('view_teams', 'Can view team details')],
            },
        ),
        migrations.CreateModel(
            name='TeamList',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('playerTeam', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('playerName', models.CharField(max_length=100)),
                ('role', models.CharField(choices=[('WK', 'Wicket Keeper'), ('BWL', 'Bowler'), ('BAT', 'Batsman')], max_length=3, null=True)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.team')),
            ],
        ),
    ]
