# Generated by Django 4.2.7 on 2023-12-14 23:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_listing_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bid',
            old_name='creator',
            new_name='bidder',
        ),
        migrations.AddField(
            model_name='listing',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='listing',
            name='wathchlist',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
