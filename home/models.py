from django.db import models
from django.utils import timezone


class Contact(models.Model):
    full_name = models.CharField(max_length=128, blank=False, null=False)
    email = models.EmailField(max_length=128, blank=False, null=False)
    message = models.TextField(max_length=1000, blank=False, null=False)
    date_recieved = models.DateTimeField(blank=False, null=False)
    unread = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        if not self.pk:
            self.date_recieved = timezone.now()
        return super(Contact, self).save(*args, **kwargs)
