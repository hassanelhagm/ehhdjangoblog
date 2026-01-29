from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class category(models.Model):
    category_name = models.CharField(max_length=50 , unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updted_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name

STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
)           

class blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    featured_image = models.ImageField(upload_to='uploads/%Y/%m/%d/', null=True, blank=True)
    short_description  = models.TextField(max_length=500)
    blog_body = models.TextField(max_length=2000)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   

    def __str__(self):
        return self.title


