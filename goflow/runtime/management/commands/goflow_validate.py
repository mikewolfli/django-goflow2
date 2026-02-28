#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand

from goflow.workflow.models import Process, Transition


class Command(BaseCommand):
    help = 'Validate workflow graphs for basic modeling rules.'

    def handle(self, *args, **options):
        errors = 0
        for process in Process.objects.all():
            transitions = Transition.objects.filter(process=process)
            activity_ids = {str(a.id) for a in process.activities.all()}
            incoming = {str(a.id): 0 for a in process.activities.all()}
            outgoing = {str(a.id): 0 for a in process.activities.all()}
            for transition in transitions:
                input_id = str(transition.input_id)
                output_id = str(transition.output_id)
                outgoing[input_id] = outgoing.get(input_id, 0) + 1
                incoming[output_id] = incoming.get(output_id, 0) + 1
                if input_id == output_id:
                    self.stdout.write(self.style.ERROR('Process %s: transition %s has self-loop' % (process.title, transition.id)))
                    errors += 1
            if not process.begin_id or str(process.begin_id) not in activity_ids:
                self.stdout.write(self.style.ERROR('Process %s: missing begin activity' % process.title))
                errors += 1
            if not process.end_id or str(process.end_id) not in activity_ids:
                self.stdout.write(self.style.ERROR('Process %s: missing end activity' % process.title))
                errors += 1
            if process.begin_id and incoming.get(str(process.begin_id), 0) > 0:
                self.stdout.write(self.style.ERROR('Process %s: begin activity has incoming transitions' % process.title))
                errors += 1
            if process.end_id and outgoing.get(str(process.end_id), 0) > 0:
                self.stdout.write(self.style.ERROR('Process %s: end activity has outgoing transitions' % process.title))
                errors += 1

        if errors:
            raise SystemExit(1)
        self.stdout.write(self.style.SUCCESS('All workflow graphs passed validation.'))
