# Generated by Django 4.1.3 on 2022-12-02 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, null=True)),
                ('address', models.CharField(max_length=500, null=True)),
                ('phone', models.CharField(max_length=18, null=True)),
                ('email', models.CharField(max_length=250, null=True)),
                ('createdDate', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
