from django.contrib import admin
from .models import About
from .models import SocialLink


# Register your models here.
class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Allow adding only if there are no About instances
        # if About.objects.exists():
        #     return False
        # return super().has_add_permission(request)
        count = About.objects.count()
        if count == 0:
            return True
        return False    




admin.site.register(About, AboutAdmin)
admin.site.register(SocialLink)

