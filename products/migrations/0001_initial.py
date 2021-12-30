# Generated by Django 4.0 on 2021-12-30 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductItem',
            fields=[
                ('ProductId', models.AutoField(primary_key=True, serialize=False)),
                ('ProductName', models.CharField(blank=True, max_length=50, null=True)),
                ('ProductPrice', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
