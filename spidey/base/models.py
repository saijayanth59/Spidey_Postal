from django.db import models

# Create your models here.
class Stamp(models.Model):
    image_url = models.CharField(max_length=500)
    postal_circle = models.CharField(max_length=255)
    # title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.description.split("was issued")[0].strip().split(' on ')[-1]
    