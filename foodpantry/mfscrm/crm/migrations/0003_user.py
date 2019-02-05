# Generated by Django 2.0.5 on 2019-02-04 23:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_product_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('password2', models.CharField(max_length=100)),
                ('last_login', models.DateTimeField(auto_now_add=True)),
                ('is_superuser', models.BooleanField()),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.TextField()),
                ('email', models.CharField(max_length=100)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
