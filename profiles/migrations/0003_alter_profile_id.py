# Generated by Django 5.0 on 2024-01-03 07:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("profiles", "0002_auto_20231026_1617"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
