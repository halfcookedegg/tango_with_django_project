from django import template
from django.utils.safestring import mark_safe
from rango.models import Category

register = template.Library()


def muv(v1,v2,v3):
    return v1*v2*v3

def my_input(v1,v2):
    temp_html = '''<div class="input-group mb-3">
                   <span class="input-group-text" id="%s">@</span>
                   <input type="text" class="form-control" placeholder="%s" aria-label="Username" >
                   </div>'''%(v1,v2)
    return mark_safe(temp_html)
@register.inclusion_tag('rango/categories.html')
def get_category_list():
 return {'categories': Category.objects.all()}