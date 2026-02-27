#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

#from goflow.workflow.decorators import allow_tags
from django.utils.safestring import mark_safe
from goflow.workflow.models import Process, Activity


class Image(models.Model):
    file = models.ImageField(upload_to='images')
    info = models.CharField(max_length=100, null=True, blank=True)
    
    #@allow_tags
    def graphic(self):
        return mark_safe('<img name=image%d src=%s>' % (self.id, self.file.url))

    def __str__(self):
        return self.info or ''

class Graph(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    background = models.ForeignKey(
        'Visual', on_delete=models.CASCADE, null=True, blank=True, related_name='bg_graphes')
    def __str__(self):
        return self.name

class MetaGraph(models.Model):
    template = models.ForeignKey(Graph, on_delete=models.CASCADE)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    content_type = models.ManyToManyField(ContentType)

    parent_attr = models.CharField(max_length=50, default='parent')
    children_attr = models.CharField(max_length=50, default='children')
    position_method = models.CharField(max_length=50, default='position')
    zorder_method = models.CharField(max_length=50, default='zorder')
    moveable_method = models.CharField(max_length=50, default='is_moveable')

class Visual(models.Model):
    x = models.PositiveSmallIntegerField(default=0)
    y = models.PositiveSmallIntegerField(default=0)
    w = models.PositiveSmallIntegerField(default=0)
    h = models.PositiveSmallIntegerField(default=0)
    need_update = models.BooleanField(default=True)
    visible = models.BooleanField(default=True)
    z = models.PositiveSmallIntegerField(default=0)
    image = models.ForeignKey(
        Image, on_delete=models.CASCADE, null=True, blank=True)
    
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    
    graph = models.ForeignKey(Graph, on_delete=models.CASCADE)

    #@allow_tags
    def graphic(self):
        return mark_safe('<img src=%s>' % self.image.file.url)
