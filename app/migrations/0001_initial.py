# Generated by Django 3.2.9 on 2021-12-29 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CONTACT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.EmailField(max_length=122)),
                ('subject', models.CharField(max_length=122)),
                ('message', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='PRODUCT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('description', models.TextField()),
                ('image', models.ImageField(default='', upload_to='static/images')),
            ],
        ),
        migrations.CreateModel(
            name='PRODUCT_DETAILS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('extra', models.CharField(choices=[('A', 'EXTRA A'), ('B', 'EXTRA B'), ('C', 'EXTRA C')], max_length=3)),
            ],
        ),
    ]