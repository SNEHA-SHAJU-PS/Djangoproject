from django.db import models

class place(models.Model):
    name=models.CharField(max_length=200)
    desc=models.TextField()
    image=models.ImageField(upload_to="images/places",null=True,blank=True)
def __str__(self):
    return self.name
