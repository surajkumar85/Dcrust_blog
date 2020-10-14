from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

class Post(models.Model):
    title = models.CharField(max_length = 100)
    image = models.ImageField(null = True,upload_to='post_pics')
    content = models.TextField()
    time_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})

    # def save(self,*args,**kawrgs):
    #     super().save(*args,**kawrgs)

    #     img = Image.open(self.image.path)

    #     if img.height > 450 or img.width > 600 :
    #         output_size = (450,600)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path) 

