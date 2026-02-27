from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('workflow', '0004_alter_transition_condition'),
    ]

    operations = [
        migrations.AddField(
            model_name='process',
            name='tenant_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='process',
            name='org_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
