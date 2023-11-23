from django.contrib import admin

from .models import Menu


admin.site.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ["name", "url", "parent"]
    list_filter = ["parent"]
    search_fields = ["name", "url"]
    # prepopulated_fields = {"url": ["name"]}
