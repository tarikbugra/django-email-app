from django.db import models

# Create your models here.
class EmailContact(models.Model):
    name = models.TextField()
    email = models.EmailField()
    message = models.TextField()
    subject = models.CharField(max_length=255)

    def __str__(self):
        return self.name