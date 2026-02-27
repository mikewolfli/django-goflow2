import json
import hmac
import hashlib
from urllib import request
from django.conf import settings


def _parse_event_types(event_types):
    if not event_types:
        return []
    return [item.strip() for item in event_types.split(',') if item.strip()]


def _event_allowed(endpoint, action):
    event_types = _parse_event_types(endpoint.event_types)
    if not event_types:
        return True
    if '*' in event_types:
        return True
    return action in event_types


def _build_payload(event):
    return {
        'id': event.id,
        'action': event.action,
        'created_at': event.created_at.isoformat(),
        'actor_id': event.actor_id,
        'process_id': event.process_id,
        'instance_id': event.instance_id,
        'workitem_id': event.workitem_id,
        'activity_id': event.activity_id,
        'transition_id': event.transition_id,
        'status_from': event.status_from,
        'status_to': event.status_to,
        'metadata': event.metadata or {},
    }


def dispatch_webhooks(event):
    from goflow.runtime.models import WebhookEndpoint

    timeout = getattr(settings, 'GOFLOW_WEBHOOK_TIMEOUT', 5)
    endpoints = WebhookEndpoint.objects.filter(enabled=True)
    for endpoint in endpoints:
        if not _event_allowed(endpoint, event.action):
            continue
        payload = _build_payload(event)
        body = json.dumps(payload).encode('utf-8')
        headers = {'Content-Type': 'application/json'}
        if endpoint.headers:
            headers.update(endpoint.headers)
        if endpoint.secret:
            signature = hmac.new(
                endpoint.secret.encode('utf-8'),
                body,
                hashlib.sha256,
            ).hexdigest()
            headers['X-Goflow-Signature'] = signature
        req = request.Request(endpoint.url, data=body, headers=headers, method='POST')
        try:
            request.urlopen(req, timeout=endpoint.timeout_seconds or timeout)
        except Exception:
            # Suppress webhook failures to avoid blocking workflow execution.
            continue
