from django.db import models

# Create your models here.

class Blog(models.Model):

    def summary(self):
        return self.body[:100]
    
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()


