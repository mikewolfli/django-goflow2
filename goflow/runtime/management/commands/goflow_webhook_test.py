#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand

from goflow.runtime.audit import log_audit_event


class Command(BaseCommand):
    help = 'Emit a test audit event to trigger webhook deliveries.'

    def add_arguments(self, parser):
        parser.add_argument('--action', default='test.ping', help='Audit action name')

    def handle(self, *args, **options):
        action = options.get('action') or 'test.ping'
        event = log_audit_event(action=action, metadata={'test': True})
        if not event:
            self.stdout.write(self.style.WARNING('No audit event emitted (audit disabled?).'))
            return
        self.stdout.write(self.style.SUCCESS('Webhook test event emitted: %s' % event.id))
