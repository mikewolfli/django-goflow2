#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from goflow.apptools.models import DefaultAppModel
from goflow.runtime.models import ProcessInstance


class Command(BaseCommand):
    help = 'Create simulation instances for a process using DefaultAppModel.'

    def add_arguments(self, parser):
        parser.add_argument('--process', required=True, help='Process name or code')
        parser.add_argument('--count', type=int, default=1, help='Number of instances')
        parser.add_argument('--user', default=None, help='Username to use as requester')

    def handle(self, *args, **options):
        process_name = options['process']
        count = options['count']
        username = options['user']

        User = get_user_model()
        if username:
            user = User.objects.get(username=username)
        else:
            user = User.objects.filter(is_superuser=True).first() or User.objects.first()
        if not user:
            self.stdout.write(self.style.ERROR('No users available to start simulation.'))
            return

        for _ in range(count):
            obj = DefaultAppModel.objects.create(history='Init')
            ProcessInstance.objects.start(process_name, user, obj, title='simulation')
        self.stdout.write(self.style.SUCCESS('Created %s simulation instance(s).' % count))
