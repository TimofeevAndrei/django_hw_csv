# Generated by Django 3.1.2 on 2023-03-29 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=0, max_digits=12)),
                ('image', models.CharField(max_length=1000)),
                ('release_date', models.CharField(max_length=50)),
                ('lte_exists', models.BooleanField()),
                ('slug', models.SlugField(max_length=200)),
            ],
        ),
    ]
