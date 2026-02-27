#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.contenttypes.models import ContentType
from goflow.workflow.models import Process, Activity
#from goflow.workflow.decorators import allow_tags
from django.utils.safestring import mark_safe

class ProcessImage(models.Model):
    process = models.ForeignKey(Process, on_delete=models.CASCADE)
    file = models.ImageField(upload_to='images')
    
    #@allow_tags
    def graphic(self):
        return mark_safe('<img name=image%d src=%s>' % (self.id, self.file.url))

    #@allow_tags
    def graphic_input(self):
        return mark_safe('<input type=image name=process src=%s>' % self.file.url)
    
    def list_activities(self):
        return self.process.activities.all()
    
    def list_activity_positions(self):
        return ActivityPosition.objects.filter(diagram=self)
        
    def __str__(self):
        return self.process.title

class ActivityPosition(models.Model):
    diagram = models.ForeignKey(ProcessImage, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    x = models.PositiveSmallIntegerField(default=0)
    y = models.PositiveSmallIntegerField(default=0)
