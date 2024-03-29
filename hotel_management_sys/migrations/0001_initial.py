# Generated by Django 3.2.5 on 2021-08-09 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('number', models.IntegerField()),
                ('type', models.CharField(choices=[('SIN', 'Single'), ('DOU', 'Double'), ('TRI', 'Triple'), ('TWI', 'Twin')], max_length=3)),
                ('beds', models.IntegerField()),
                ('capacity', models.IntegerField()),
            ],
            options={
                'db_table': 'hotel_room',
            },
        ),
    ]
