# Generated by Django 5.0.6 on 2024-06-25 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0005_alter_categorymodel_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='post_name',
            field=models.CharField(db_index=True, max_length=100, unique=True),
        ),
    ]
