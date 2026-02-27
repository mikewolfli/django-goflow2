from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


def set_process_code(apps, schema_editor):
    Process = apps.get_model('workflow', 'Process')
    for process in Process.objects.all():
        if not process.code:
            process.code = process.title
            process.save(update_fields=['code'])


class Migration(migrations.Migration):
    dependencies = [
        ('workflow', '0002_workflowlayout'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='process',
            name='code',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='process',
            name='version',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='process',
            name='status',
            field=models.CharField(choices=[('draft', 'draft'), ('published', 'published'), ('retired', 'retired')], default='published', max_length=10),
        ),
        migrations.AddField(
            model_name='process',
            name='published_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='process',
            name='published_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='published_processes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='process',
            name='version_note',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='allowed_groups',
            field=models.ManyToManyField(blank=True, related_name='allowed_activities', to='auth.group'),
        ),
        migrations.AddField(
            model_name='activity',
            name='allowed_users',
            field=models.ManyToManyField(blank=True, related_name='allowed_activities', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='activity',
            name='sla_duration',
            field=models.CharField(blank=True, help_text='SLA duration, e.g. 3d, 12h, 45m', max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='sla_warn',
            field=models.CharField(blank=True, help_text='SLA warning threshold, e.g. 2d, 8h', max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='sla_roles',
            field=models.ManyToManyField(blank=True, related_name='sla_activities', to='auth.group'),
        ),
        migrations.AddField(
            model_name='activity',
            name='compensation_handler',
            field=models.CharField(blank=True, help_text='Callable path for compensation handler', max_length=255, null=True),
        ),
        migrations.RunPython(set_process_code, migrations.RunPython.noop),
    ]
