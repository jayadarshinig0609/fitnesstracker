# Generated by Django 4.1.6 on 2023-04-03 14:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("exercises", "0002_rename_exercise_exercises"),
    ]

    operations = [
        migrations.AlterField(
            model_name="exercises",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="exercises",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
