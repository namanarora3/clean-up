from django.contrib import admin

# Register your models here.
from .models import Tasks,Location,Category
admin.site.register(Tasks)
admin.site.register(Category)
admin.site.register(Location)