# Generated by Django 5.1.3 on 2024-11-23 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0005_uploaditem_item_sha_hash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploaditem',
            name='imgUrl',
            field=models.TextField(default='fsdaf'),
            preserve_default=False,
        ),
    ]
