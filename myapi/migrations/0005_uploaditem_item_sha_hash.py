# Generated by Django 5.1.3 on 2024-11-23 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0004_remove_item_description_remove_item_imageurl_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgUrl', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='sha_hash',
            field=models.CharField(default=1, max_length=64),
            preserve_default=False,
        ),
    ]