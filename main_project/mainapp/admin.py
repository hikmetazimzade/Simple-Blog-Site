from django.contrib import admin
from blogapp.models import CategoryModel, BlogModel, CommentModel
from .models import AboutModel, ContactModel


# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category_name", )
    list_filter = ("category_name", )
    prepopulated_fields = {"slug" : ("category_name",),}
    

class BlogAdmin(admin.ModelAdmin):
    list_display = ("blog_name", "like_number", "user", "primary_key")
    list_display_links = ("blog_name",)
    list_filter = ("categories",)
    search_fields = ("blog_name", )

    def primary_key(self, obj):
        return obj.pk


class CommentAdmin(admin.ModelAdmin):
    list_display = ("comment_name", "user")
    list_display_links = ("comment_name",)
    list_filter = ("user",)


    def comment_name(self, obj):
        return f"{obj.blog.blog_name} Comment"


class ContactAdmin(admin.ModelAdmin):
    pass


class AboutAdmin(admin.ModelAdmin):
    pass


admin.site.register(CategoryModel, CategoryAdmin)
admin.site.register(BlogModel, BlogAdmin)
admin.site.register(CommentModel, CommentAdmin)
admin.site.register(ContactModel, ContactAdmin)
admin.site.register(AboutModel, AboutAdmin)