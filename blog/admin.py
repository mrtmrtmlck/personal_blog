from django.contrib import admin

from blog.models import Author, Label, Article

admin.site.register(Label)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'birthday',)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'display_label', 'created_at', 'modified_at',)
    readonly_fields = ('slug',)
