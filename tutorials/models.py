from django.db import models

category_choice = (
    ('slider_1', 'slider_1'),
    ('slider_2', 'slider_2'),
    ('slider_3', 'slider_3'),
    ('aboutus', 'aboutus'),
    ('businessprograms', 'businessprograms'),
    ('communication', 'communication'),
    ('consult', 'consult'),
    ('customer', 'customer'),
    ('hr', 'hr'),
    ('sales', 'sales'),
    ('special', 'special'),
    ('train', 'train'),
)

class Tutorial(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=category_choice)
    feature_image = models.ImageField(upload_to='tutorial/images/')
    attachment = models.FileField(upload_to='tutorial/attachments/')

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.feature_image.delete()
        self.attachment.delete()
        super().delete(*args, **kwargs)
