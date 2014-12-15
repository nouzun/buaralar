from ajaximage.widgets import AjaxImageWidget
from django import template
register = template.Library()

@register.filter(name='is_image')
def is_image(field):
    return field.field.field.widget.__class__.__name__ == AjaxImageWidget().__class__.__name__