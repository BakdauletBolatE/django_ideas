# Generated by Django 3.1.4 on 2021-03-02 05:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Content', '0006_icategory_ficon'),
    ]

    operations = [
        migrations.AddField(
            model_name='ideas',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Создано'),
        ),
    ]