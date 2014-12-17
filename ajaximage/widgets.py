import os
from django.forms import widgets
from django.template.loader import get_template
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse
from django.core.files.storage import default_storage
from django.template import Context

class AjaxImageWidget(widgets.TextInput):

    class Media:
        js = (
            'ajaximage/js/ajaximage.js',
            'ajaximage/js/jquery.Jcrop.min.js',
        )
        css = {
            'all': (
                'ajaximage/css/bootstrap-progress.min.css',
                'ajaximage/css/jquery.Jcrop.min.css',
                'ajaximage/css/styles.css',
            )
        }

    def __init__(self, *args, **kwargs):
        self.upload_to = kwargs.pop('upload_to', '')
        self.max_width = kwargs.pop('max_width', 0)
        self.max_height = kwargs.pop('max_height', 0)
        self.crop = kwargs.pop('crop', 0)
        super(AjaxImageWidget, self).__init__(*args, **kwargs)

    def render(self, name, value, attrs=None):
        t = get_template("ajaximage/jcrop_image_widget.html")
        final_attrs = self.build_attrs(attrs)
        element_id = final_attrs.get('id')

        kwargs = {'upload_to': self.upload_to,
                  'max_width': self.max_width,
                  'max_height': self.max_height,
                  'crop': self.crop}

        upload_url = reverse('ajaximage', kwargs=kwargs)

        # NB convert to string and do not rely on value.url
        # value.url fails when rendering form with validation errors because
        # form value is not a FieldFile. Use storage.url and file_path - works
        # with FieldFile instances and string formdata
        file_path = str(value) if value else ''
        file_url = default_storage.url(file_path) if value else ''

        file_name = os.path.basename(file_url)

        substitutions = {
            "upload_url": upload_url,
            "file_url": file_url,
            "file_name": file_name,
            "file_path": file_path,
            "element_id": element_id,
            "input_name": name,
            "image_value": value
        }

        c = Context(substitutions)

        return t.render(c)
