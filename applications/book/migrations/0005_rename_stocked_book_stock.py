# Generated by Django 3.2.10 on 2021-12-27 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_book_stocked'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='stocked',
            new_name='stock',
        ),
    ]