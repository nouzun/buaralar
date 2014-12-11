"""
Example URLConf for a contact form.

If all you want is the basic ContactForm with default behavior, just
include this URLConf somewhere in your URL hierarchy (for example, at
``/contact/``)>

"""

from django.conf.urls import patterns
from django.conf.urls import url
from django.views.generic import TemplateView

from contact.views import ContactFormView


urlpatterns = patterns('',
                       url(r'^$', ContactFormView.as_view(), name='contact'),
                       url(r'^sent/$', TemplateView.as_view(template_name='contact/contact_form_sent.html'), name='contact_form_sent'),
                       )