# Generated by Django 5.0.3 on 2024-03-27 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_guy_figurine'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='figurine',
            options={'verbose_name': 'Figurine', 'verbose_name_plural': 'Figurines'},
        ),
        migrations.AddField(
            model_name='figurine',
            name='liked',
            field=models.BooleanField(default=False),
        ),
    ]
