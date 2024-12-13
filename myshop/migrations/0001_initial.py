# Generated by Django 5.1.4 on 2024-12-13 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Description', models.TextField()),
                ('price', models.DecimalField(decimal_places=3, max_digits=10)),
                ('Image', models.ImageField(upload_to='images')),
            ],
        ),
    ]
