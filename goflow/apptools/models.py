#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from goflow.workflow.models import Transition
#from goflow.workflow.decorators import allow_tags
from django.utils.safestring import mark_safe
from django.conf import settings
from django.utils.translation import gettext_lazy as _, gettext


class DefaultAppModel(models.Model):
    """Default implementation object class  for process instances.
    
    When a process instance starts, the instance has to carry an
    implementation object that contains the application data. The
    specifications for the implementation class is:
    
    (nothing: now managed by generic relation)
    
    This model is used in process simulations: you don't have to define
    application in activities for this; the DefaultAppModel is used
    to keep workflow history for displaying to users.
    """
    history = models.TextField(_('history'), editable=False, null=True, blank=True)
    comment = models.TextField(_('comment'), null=True, blank=True)
    
    def __str__(self):
        return gettext('simulation model %s') % str(self.id)
    class Admin:
        list_display = ('__str__',)
    class Meta:
        verbose_name=_('Simulation object')

class Image(models.Model):
    '''
    An image stored in the database
    '''
    category = models.CharField(_('category'), max_length=20, null=True, blank=True)
    file = models.ImageField(_('file'), upload_to='images')
    
    def url(self):
        return "%s%s" % (settings.MEDIA_URL, self.file)
    
    #@allow_tags
    def graphic(self):
        '''
        generates an *img* html tag for html rendering
        '''
        return mark_safe('<img name="image%d" src="%s">' % (self.pk, self.url()))
    
    #@allow_tags
    def graphic_input(self):
        '''
        generates an *input* html tag with type=image for html rendering
        '''
        return mark_safe('<input type=image name=icon src=%s>' % self.url())
    
    def __str__(self):
        return str(self.file)

    class Meta:
        verbose_name=_('Image')

class Icon(models.Model):
    '''
    An image accessible by an url.

    Tip: all of the "Image" objects can be imported as "Icon" from the
    admin panel.
    '''
    category = models.CharField(_('catagory'), max_length=20, null=True, blank=True)
    # url = models.URLField(verify_exists=False)
    url = models.URLField()
    
    #@allow_tags
    def graphic(self):
        '''
        generates an *img* html tag for html rendering
        '''
        return mark_safe('<img name="image%d" src="%s">' % (self.pk, self.url))
    
    #@allow_tags
    def graphic_input(self):
        '''
        generates an *input* html tag with type=image for html rendering
        '''
        return mark_safe('<input type=image name=icon src="%s">' % self.url)
    
    def __str__(self):
        return self.url

    class Meta:
        verbose_name=_('Icon')

class ImageButton(models.Model):
    '''
    Mapping object between an "action" and an "Icon".
    
    ImageButton objects have also a textual field: label.
    '''
    action = models.SlugField(primary_key=True,verbose_name=_('action'))
    label = models.CharField(_('label'), max_length=100)
    icon = models.ForeignKey(Icon, on_delete=models.CASCADE, verbose_name=_('icon'))
    
    #@allow_tags
    def graphic(self):
        '''
        generates an *img* html tag for html rendering
        '''
        return mark_safe('<img name="image-%s" src="%s">' % (self.pk, self.icon.url))
    
    #@allow_tags
    def graphic_input(self):
        '''
        generates an *input* html tag with type=image for html rendering
        '''
        return mark_safe('<input type=image name=image src="%s" value="%s" title="%s">' % (self.icon.url, self.pk, self.label))
    
    def __str__(self):
        return self.label

    class Meta:
        verbose_name=_("Image Button")
