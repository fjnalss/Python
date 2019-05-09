from django.contrib import admin

from .models import Article, Category, Tag

'''
class CategoryInline(admin.TabularInline):
	model = Category
	extra = 2


class TagInline(admin.TabularInline):
	model = Tag
	extra = 2
'''

class ArticleAdmin(admin.ModelAdmin):
	list_display = ['title', 'create_time', 'modified_time','category', 'author']



admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Tag)

