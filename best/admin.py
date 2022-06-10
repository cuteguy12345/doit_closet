from django.contrib import admin
from .models import Best, Category
# Register your models here.

admin.site.register(Best)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Category, CategoryAdmin)