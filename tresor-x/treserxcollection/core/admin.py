from django.contrib import admin
from core.models import Figurine, Category


# Register your models here.
class FigurineAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'price', 'have_it', 'liked')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Figurine, FigurineAdmin)
admin.site.register(Category, CategoryAdmin)
