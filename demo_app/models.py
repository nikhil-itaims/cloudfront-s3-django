from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    image_url = models.ImageField(upload_to='blogs/')

    def delete(self):
        self.image_url.delete()
        super().delete()