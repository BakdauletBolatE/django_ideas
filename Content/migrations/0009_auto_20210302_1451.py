# Generated by Django 3.1.4 on 2021-03-02 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Content', '0008_auto_20210302_0819'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ideas',
            name='rating',
        ),
        migrations.AddField(
            model_name='rating',
            name='idea',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Content.ideas'),
        ),
    ]
