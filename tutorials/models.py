from django.db import models

MEDIA_CHOICES = [
    ('HomePage', (
        ('Slider 1', 'Slider 1'),
        ('Slider 2', 'Slider 2'),
        ('Slider 3', 'Slider 3'),
        ('BusinessPrograms', 'BusinessPrograms'),
        ('Communication', 'Communication'),
        ('Consult', 'Consult'),
        ('Customer', 'Customer'),
        ('HR', 'HR'),
        ('Sales', 'Sales'),
        ('Special', 'Special'),
        ('Train', 'Train'),
        )
    ),
    ('About Us', (
        ('AboutUs', 'AboutUs'),
        )
    ),
]
class Tutorial(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=MEDIA_CHOICES)
    feature_image = models.ImageField(upload_to='tutorial/images/')
    attachment = models.FileField(upload_to='tutorial/attachments/')

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.feature_image.delete()
        self.attachment.delete()
        super().delete(*args, **kwargs)

class Monitor(models.Model):
    continent = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    capital = models.CharField(max_length=50, blank=True, null=True)
    datetime = models.CharField(max_length=50, blank=True, null=True)
    ip = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.ip
