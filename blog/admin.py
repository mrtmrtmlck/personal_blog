from django.contrib import admin

from blog.models import Label, Article

admin.site.register(Label)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'display_label', 'created_at', 'modified_at',)
    readonly_fields = ('slug',)
