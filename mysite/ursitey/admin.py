from django.contrib import admin
# Author of the post
from django.db import models
from django.forms import TextInput, Textarea

from .models import Post

class Admposts(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'35'})},
        models.TextField: {'widget': Textarea(attrs={'rows':10, 'cols':40})},
    }

admin.site.register(Post, Admposts)




