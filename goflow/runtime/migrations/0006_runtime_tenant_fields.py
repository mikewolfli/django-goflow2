from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('runtime', '0005_locking_versions'),
    ]

    operations = [
        migrations.AddField(
            model_name='processinstance',
            name='tenant_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='processinstance',
            name='org_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='workitem',
            name='tenant_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='workitem',
            name='org_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
