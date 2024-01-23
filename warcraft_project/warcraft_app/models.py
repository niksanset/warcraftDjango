from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class Audio(models.Model):
    title = models.CharField(max_length=255,blank=True)
    audio = models.FileField(upload_to='audio/',
                             null=True,
                             blank=True)
    category = models.ForeignKey(Category, 
                                 on_delete = models.CASCADE,
                                 blank=True)
    def __str__(self):
        return f"{self.title}"
    


class Image(models.Model):
    title = models.CharField(max_length=255,blank=True)
    image = models.ImageField(upload_to='images/',
                              null=True,
                              blank=True)
    
    def __str__(self):
        return f"{self.title}"
    

class Video(models.Model):
    title = models.CharField(max_length=255,blank=True)
    video = models.FileField(upload_to='video/',
                             null=True,
                             blank=True)
    category = models.ForeignKey(Category, 
                                 on_delete = models.CASCADE,
                                 blank=True)
    def __str__(self):
        return f"{self.title}"



