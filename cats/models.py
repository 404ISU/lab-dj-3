from django.db import models
class CatImage(models.Model):
    name=models.CharField(max_length=255)
    image=models.ImageField(upload_to='cat_images')
    def __str__(self):
        return self.name
# Create your models here.
