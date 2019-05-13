from ..models import Article, Category
from django import template

register = template.Library()

#最新文章模板标签
@register.simple_tag
def get_recent_article(num=5):
	return Article.objects.all().order_by('-create_time')[:num]

#按月归档模板标签
@register.simple_tag
def archives():
	return Article.objects.dates('create_time', 'month', order='DESC')

#分类模板标签
@register.simple_tag
def get_categories():
	return Category.objects.all()

