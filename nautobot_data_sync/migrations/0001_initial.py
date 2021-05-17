# Generated by Django 3.1.11 on 2021-05-17 18:39

import django.core.serializers.json
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('extras', '0005_configcontext_device_types'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sync',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('_custom_field_data', models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('dry_run', models.BooleanField(default=False)),
                ('diff', models.JSONField()),
                ('job_result', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='extras.jobresult')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='SyncLogEntry',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('action', models.CharField(max_length=32)),
                ('status', models.CharField(max_length=32)),
                ('diff', models.JSONField()),
                ('changed_object_id', models.UUIDField(blank=True, null=True)),
                ('object_repr', models.CharField(editable=False, max_length=200)),
                ('message', models.CharField(blank=True, max_length=511)),
                ('changed_object_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='contenttypes.contenttype')),
                ('object_change', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='extras.objectchange')),
                ('sync', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', related_query_name='log', to='nautobot_data_sync.sync')),
            ],
            options={
                'verbose_name_plural': 'sync log entries',
                'ordering': ['sync', 'timestamp'],
            },
        ),
    ]
