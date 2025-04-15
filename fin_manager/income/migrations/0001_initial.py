# Generated by Django 5.1.7 on 2025-04-11 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.CharField(choices=[('salary', 'Salary'), ('freelance', 'Freelance'), ('business', 'Business'), ('investment', 'Investment'), ('social', 'Social'), ('other', 'Other')], default='other', max_length=20)),
                ('date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
