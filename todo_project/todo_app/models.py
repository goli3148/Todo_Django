from django.db import models

class todo(models.Model):
    
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
    
    date_pub = models.DateField("date published", auto_now_add=True)
    date_upd = models.DateField("date updated", auto_now=True)
    
    def __str__(self):
        return self.subject
    

# Create your models here.
