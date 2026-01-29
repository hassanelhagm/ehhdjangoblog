from django.contrib import admin
from .models import blog

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

    list_display = ('title', 'author', 'category', 'is_featured', 'created_at')
    list_editable = ('is_featured',)
    # list_filter = ('status', 'is_featured', 'created_at', 'category')
    search_fields = ('id','title', 'author__username','category__category_name', 'status', 'blog_body')
    # prepopulated_fields = {'slug': ('title',)}
    # ordering = ('-created_at',)

# Register your models here.
from .models import category
admin.site.register(category)
admin.site.register(blog, BlogAdmin)