from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class ContactModel(models.Model):
    content = RichTextUploadingField()

    def __str__(self):
        return str(self.pk)
    
    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contact Us Page"


class AboutModel(models.Model):
    content = RichTextUploadingField()


    def __str__(self):
        return str(self.pk)
    

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "About Us Page"