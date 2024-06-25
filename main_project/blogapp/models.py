from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models.signals import post_delete
from django.dispatch import receiver
import os
from django.conf import settings
# from ckeditor.fields import RichTextField


class CategoryModel(models.Model):
    category_name = models.CharField(max_length = 50, unique = True, default = "Other")
    slug = models.SlugField(max_length = 100, null = False, db_index = True, unique = True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super(CategoryModel, self).save(*args, **kwargs)


    def __str__(self) -> str:
         return self.category_name
    

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class BlogModel(models.Model):
    blog_name = models.CharField(max_length = 100, unique = True, null = False, blank = False, db_index = True)
    like_number = models.IntegerField(default = 0)
    content = RichTextUploadingField()
    categories = models.ManyToManyField(CategoryModel)
    user = models.ForeignKey(User, default = None, null = True, on_delete = models.CASCADE, db_index = True)


    def __str__(self):
         return self.blog_name
    

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"
    

class CommentModel(models.Model):
    content = models.TextField()
    star_number = models.IntegerField(default = 5)
    blog = models.ForeignKey(BlogModel, on_delete = models.CASCADE)
    user = models.ForeignKey(User, default = None, null = True, on_delete = models.CASCADE)


    def __str__(self):
        return self.blog.blog_name + " Comment"


    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"


def delete_associated_files(instance):
    content = instance.content
    media_root = settings.MEDIA_ROOT
    for filepath in find_image_paths(content):
        full_path = os.path.join(media_root, filepath.lstrip('/'))
        if os.path.exists(full_path):
            os.remove(full_path)


def find_image_paths(content):
    import re
    image_urls = re.findall(r'/files/user_files/[\w\-]+\.\w+', content)
    return image_urls


@receiver(post_delete, sender=BlogModel)
def delete_images(sender, instance, **kwargs):
    delete_associated_files(instance)