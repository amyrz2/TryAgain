# Generated by Django 4.1.2 on 2022-12-13 02:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Deceased',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deceased_first_name', models.CharField(max_length=30)),
                ('deceased_last_name', models.CharField(max_length=30)),
                ('deceased_gender', models.CharField(max_length=1)),
                ('deceased_birth_date', models.DateField(help_text="Deceased's birthday")),
                ('deceased_birth_city', models.CharField(max_length=30)),
                ('deceased_birth_state', models.CharField(max_length=30)),
                ('deceased_birth_country', models.CharField(max_length=30)),
                ('deceased_death_date', models.DateField(help_text="Deceased's deathday")),
                ('deceased_death_city', models.CharField(max_length=30)),
                ('deceased_death_state', models.CharField(max_length=30)),
                ('deceased_death_country', models.CharField(max_length=30)),
                ('deceased_biography', models.CharField(max_length=20000)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
