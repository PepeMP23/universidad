# Generated by Django 4.2.6 on 2023-10-09 03:55

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("estudiantes", "0004_alter_inscripcion_id_curso"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="inscripcion",
            options={"verbose_name_plural": "Inscripciones"},
        ),
    ]
