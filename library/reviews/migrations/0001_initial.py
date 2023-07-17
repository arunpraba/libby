# Generated by Django 4.2.3 on 2023-07-16 23:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catelog', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Published date')),
                ('comment', models.TextField(max_length=1024)),
                ('value', models.IntegerField(choices=[(5, '5'), (4, '4'), (3, '3'), (2, '2'), (1, '1')], default=5)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catelog.book')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Review',
                'verbose_name_plural': 'Reviews',
                'ordering': ['-pub_date'],
            },
        ),
    ]
