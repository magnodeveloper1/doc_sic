from django import template
from django.contrib.admin.templatetags.admin_list import result_list

register = template.Library()
register.inclusion_tag('list.html')(result_list)