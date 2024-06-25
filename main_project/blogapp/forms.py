from django import forms
from django.core.validators import MinLengthValidator
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.forms import widgets


class BlogForm(forms.Form):
    content = forms.CharField(required = True, validators = [MinLengthValidator(5, "Minimum Blog Character Length Must Be 5!")], 
                              widget = CKEditorUploadingWidget())
    

    blog_name = forms.CharField(required = True, validators = [MinLengthValidator(5, "Minimum Blog Character Length Must Be 5!")],
                                widget = widgets.TextInput(attrs = {
                                    "placeholder" : "Blog Name..."
                                }))
                              

    def clean_content(self):
        content = self.cleaned_data.get("content", "")
        return content
    
    

class CommentForm(forms.Form):
    comment = forms.CharField(required = False, validators = [MinLengthValidator(5, "Minimum Comment Character Length Must Be 5!")], 
                              widget = widgets.Textarea())
                              

    def clean_content(self):
        content = self.cleaned_data.get("comment", "")
        return content