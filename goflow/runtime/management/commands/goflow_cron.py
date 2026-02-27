#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand

from goflow.runtime.automation import run_timeout_scan


class Command(BaseCommand):
    help = 'Run GoFlow pending automation tasks (timeout forwarding).'

    def handle(self, *args, **options):
        result = run_timeout_scan()
        self.stdout.write(
            self.style.SUCCESS(
                'goflow_cron done: timeout_transitions={timeout_transitions}, checked_workitems={checked_workitems}, triggered_workitems={triggered_workitems}'.format(
                    **result
                )
            )
        )
