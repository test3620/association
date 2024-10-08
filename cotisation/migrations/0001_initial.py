# Generated by Django 5.0.6 on 2024-10-08 15:18

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Depense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=50)),
                ('montant', models.IntegerField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Entree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=50)),
                ('montant', models.IntegerField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Deces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant', models.IntegerField()),
                ('deces', models.CharField(max_length=50)),
                ('reunion', models.DateField()),
                ('paye', models.BooleanField(default=False)),
                ('membre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Don',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant', models.IntegerField()),
                ('objet', models.CharField(max_length=50)),
                ('reunion', models.DateField()),
                ('paye', models.BooleanField(default=False)),
                ('membre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Mensuel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant', models.IntegerField()),
                ('reunion', models.DateField()),
                ('lieu', models.CharField(default='Rond point Kpogli', max_length=50)),
                ('paye', models.BooleanField(default=False)),
                ('membre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MonAdhesion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant', models.IntegerField(default=15000)),
                ('reunion', models.DateField(default=django.utils.timezone.now)),
                ('lieu', models.CharField(default='Rond point Kpogli', max_length=50)),
                ('paye', models.BooleanField(default=False)),
                ('membre', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='NouveauNe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant', models.IntegerField()),
                ('enfant', models.CharField(max_length=50)),
                ('reunion', models.DateField()),
                ('paye', models.BooleanField(default=False)),
                ('membre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rejouissance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant', models.IntegerField()),
                ('date', models.DateField()),
                ('lieu', models.CharField(max_length=50)),
                ('paye', models.BooleanField(default=False)),
                ('membre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reunion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reunion', models.DateField()),
                ('presence', models.BooleanField(default=False)),
                ('retard', models.BooleanField(default=False)),
                ('permission', models.BooleanField(default=False)),
                ('absence', models.BooleanField(default=False)),
                ('membre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
