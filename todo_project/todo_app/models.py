from django.db import models
from django.conf import settings

class todo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    
    subject = models.CharField("subject", max_length=50)
    extra = models.TextField("extra", max_length=500)
    
    HIGHPRIO = 'H'
    MEDUIMPRIO = 'M'
    LOWPRIO = 'L'
    PRIORITY_CHOICES=[
        (HIGHPRIO, 'highPriority'),
        (MEDUIMPRIO, 'meduimPriority'),
        (LOWPRIO, 'lowPriority')
    ]
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default=MEDUIMPRIO)
    
    date = models.DateTimeField("date time", null=True)
    
    date_pub = models.DateField("date published", auto_now_add=True)
    date_upd = models.DateField("date updated", auto_now=True)
    
    
    
    def __str__(self):
        return self.subject
    

# Create your models here.
