# Generated by Django 3.1.7 on 2021-04-15 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dojoreadapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviews',
            name='book',
        ),
        migrations.AddField(
            model_name='reviews',
            name='book',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='book_reviews', to='dojoreadapp.books'),
            preserve_default=False,
        ),
    ]
