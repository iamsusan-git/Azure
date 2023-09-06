from django.contrib import admin
from .models import Post  # Import your Post model

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')  # Display these fields in the admin list view

# Register your Post model with the custom admin class
admin.site.register(Post, PostAdmin)
