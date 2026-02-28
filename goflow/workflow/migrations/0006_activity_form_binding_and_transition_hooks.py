from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('workflow', '0005_process_tenant_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='node_type',
            field=models.CharField(choices=[('standard', 'standard'), ('approval', 'approval'), ('review', 'review'), ('service', 'service'), ('notification', 'notification'), ('gateway', 'gateway'), ('script', 'script')], default='standard', max_length=20),
        ),
        migrations.AddField(
            model_name='activity',
            name='form_template',
            field=models.CharField(blank=True, help_text='template path for task form rendering', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='form_class',
            field=models.CharField(blank=True, help_text='callable path for a Django Form/ModelForm', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='transition',
            name='pre_hook',
            field=models.CharField(blank=True, help_text='callable path executed before transition evaluation', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='transition',
            name='post_hook',
            field=models.CharField(blank=True, help_text='callable path executed after transition evaluation', max_length=255, null=True),
        ),
    ]
