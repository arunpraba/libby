# Generated by Django 4.2.3 on 2023-07-17 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catelog', '0002_alter_book_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
