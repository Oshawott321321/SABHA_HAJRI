# Generated by Django 4.2.1 on 2023-07-09 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='date_person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_sabha', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Family',
            fields=[
                ('family_id', models.IntegerField(primary_key=True, serialize=False)),
                ('family_name', models.CharField(max_length=50)),
                ('family_head', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('details', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('p_id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=50, null=True)),
                ('gender', models.CharField(max_length=10, null=True)),
                ('address_society', models.CharField(max_length=100, null=True)),
                ('address_house_no', models.CharField(max_length=100, null=True)),
                ('mobile_no', models.CharField(max_length=15, null=True)),
                ('whatsapp_no', models.CharField(max_length=15, null=True)),
                ('old_karyakar', models.CharField(max_length=100, null=True)),
                ('karykar', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
