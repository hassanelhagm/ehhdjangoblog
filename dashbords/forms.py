from django import forms
from blogs.models import category   
from blogs.models import blog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CategoryForm(forms.ModelForm):
    class Meta:
        model = category
        fields = '__all__'  

class blogpostForm(forms.ModelForm):
    class Meta:
        model = blog
        fields = (  'title',  'category', 'short_description', 'blog_body', 'featured_image',  'status', 'is_featured' )



class AddUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'is_superuser', 'groups',  'user_permissions', 'password1', 'password2')



class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'is_superuser', 'groups',  'user_permissions')
        widgets = {
            'password': forms.PasswordInput(),  # Hide password field in edit form
        }
        help_texts = {
            'password': 'Leave blank to keep current password.',
        }