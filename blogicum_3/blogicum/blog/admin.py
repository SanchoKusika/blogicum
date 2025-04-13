from django.contrib import admin
from .models import Post, Category, Location


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'slug', 'is_published', 'created_at')
        }),
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Location)
admin.site.register(Post)

admin.site.site_title = "Админка Блога"
admin.site.site_header = "Блог"
admin.site.index_title = "Панель управления"
