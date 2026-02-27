from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("workflow", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="WorkflowLayout",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "layout",
                    models.JSONField(blank=True, default=dict),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True),
                ),
                (
                    "process",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="layout",
                        to="workflow.process",
                    ),
                ),
            ],
        ),
    ]
