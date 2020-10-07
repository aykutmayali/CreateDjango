from django.db import models

# Create your models here.
class Term(models.Model):
    details = models.CharField(max_length=500)
    last_updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.details

        