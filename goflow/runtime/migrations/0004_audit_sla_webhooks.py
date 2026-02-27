from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('workflow', '0003_process_versioning_sla_permissions'),
        ('runtime', '0003_alter_workitem_others_workitems_from'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='processinstance',
            name='process_version',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='workitem',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AddField(
            model_name='workitem',
            name='activated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='workitem',
            name='completed_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='workitem',
            name='sla_warned_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='workitem',
            name='sla_breached_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='workitem',
            name='last_escalation_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='AuditEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('action', models.CharField(max_length=50)),
                ('status_from', models.CharField(blank=True, max_length=20, null=True)),
                ('status_to', models.CharField(blank=True, max_length=20, null=True)),
                ('metadata', models.JSONField(blank=True, default=dict)),
                ('activity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='audit_events', to='workflow.activity')),
                ('actor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='audit_events', to=settings.AUTH_USER_MODEL)),
                ('instance', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='audit_events', to='runtime.processinstance')),
                ('process', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='audit_events', to='workflow.process')),
                ('transition', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='audit_events', to='workflow.transition')),
                ('workitem', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='audit_events', to='runtime.workitem')),
            ],
        ),
        migrations.CreateModel(
            name='WebhookEndpoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('enabled', models.BooleanField(default=True)),
                ('event_types', models.CharField(blank=True, help_text='Comma-separated event types, or * for all.', max_length=255, null=True)),
                ('secret', models.CharField(blank=True, max_length=255, null=True)),
                ('headers', models.JSONField(blank=True, default=dict)),
                ('timeout_seconds', models.IntegerField(default=5)),
            ],
        ),
    ]
