# Generated by Django 3.2.10 on 2021-12-21 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0002_alter_author_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='nickname',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]