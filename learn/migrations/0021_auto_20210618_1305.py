# Generated by Django 3.1.7 on 2021-06-18 07:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('learn', '0020_auto_20210618_0015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='userDetails',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
