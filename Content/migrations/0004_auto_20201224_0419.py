# Generated by Django 3.1.4 on 2020-12-24 04:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Content', '0003_auto_20201223_0837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='ideas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photo', to='Content.ideas'),
        ),
    ]
