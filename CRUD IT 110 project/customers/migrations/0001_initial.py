# Generated by Django 4.0.4 on 2022-06-30 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('middlename', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('customer_address', models.CharField(max_length=100)),
                ('date_added', models.DateTimeField()),
                ('date_updated', models.DateTimeField()),
            ],
        ),
    ]