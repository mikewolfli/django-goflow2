from django.db import models
from django.conf import settings

class SampleModel(models.Model):
    '''
    a model with usual fields used as a typical workflow object.
    '''
    date = models.DateField(auto_now_add=True)
    text = models.CharField(max_length = 100)
    number = models.IntegerField(null=True, blank=True)
    requester = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='requester')
    
    def __str__(self):
        return self.text
