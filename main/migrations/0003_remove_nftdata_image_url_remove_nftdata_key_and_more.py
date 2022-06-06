# Generated by Django 4.0.5 on 2022-06-06 12:26

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_nft_data_nftdata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nftdata',
            name='image_url',
        ),
        migrations.RemoveField(
            model_name='nftdata',
            name='key',
        ),
        migrations.AddField(
            model_name='nftdata',
            name='data',
            field=jsonfield.fields.JSONField(blank=True, null=True),
        ),
    ]
