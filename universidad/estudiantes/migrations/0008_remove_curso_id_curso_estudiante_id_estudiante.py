# Generated by Django 4.2.6 on 2023-10-09 04:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("estudiantes", "0007_curso_id_curso"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="curso",
            name="id_curso",
        ),
        migrations.AddField(
            model_name="estudiante",
            name="id_estudiante",
            field=models.IntegerField(null=True),
        ),
    ]
