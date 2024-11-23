from django.db import models

class Item(models.Model):
    image = models.TextField(null=False)  
    md5_hash = models.CharField(max_length=32)
    sha_hash = models.CharField(max_length=64)
    phash = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name


