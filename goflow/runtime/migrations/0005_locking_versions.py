from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('runtime', '0004_audit_sla_webhooks'),
    ]

    operations = [
        migrations.AddField(
            model_name='processinstance',
            name='version',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='workitem',
            name='version',
            field=models.IntegerField(default=1),
        ),
    ]
