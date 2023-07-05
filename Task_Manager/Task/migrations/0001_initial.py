# Generated by Django 4.2.3 on 2023-07-05 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Description', models.TextField()),
                ('Creation_date', models.DateField()),
                ('End_date', models.DateField()),
                ('Priority', models.CharField(choices=[('sm', 'Малый'), ('md', 'Средний'), ('hg', 'Высокий')], max_length=50)),
                ('Status', models.CharField(choices=[('true', 'Сделано'), ('false', 'Не Сделано')], max_length=50)),
            ],
        ),
    ]