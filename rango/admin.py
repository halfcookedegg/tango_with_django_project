from django.contrib import admin
from rango.models import Page, Category
from rango.models import UserProfile


class PageAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'url')

admin.site.register(Page, PageAdmin)
admin.site.register(Category)
admin.site.register(UserProfile)

