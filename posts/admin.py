from django.contrib import admin
from django.contrib.admin import forms
from posts.models import Post, Category, Event, Place, Ad
import datetime

# class EventAdminForm(forms.Form):
#     class Meta:
#         model = Event
#
#     def clean(self):
#         date = self.cleaned_data['event_date_begin']
#         if date < datetime.date.today():
#             raise forms.ValidationError("The date cannot be in the past!")
#         return date

class EventInline(admin.TabularInline):
    model = Event
    extra = 1

class EventAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title_text']}),
        ('Category',         {'fields': ['category']}),
        ('Description',      {'fields': ['description_text']}),
        ('Location',         {'fields': ['location_text']}),
        ('Price',            {'fields': ['price']}),
        ('Start Date',       {'fields': ['event_date_begin'], 'classes': ['collapse']}),
        ('End Date',         {'fields': ['event_date_end'], 'classes': ['collapse']}),
    ]
    inlines = [EventInline]
    list_display = ('title_text', 'description_text', 'location_text', 'price', 'event_date_begin', 'event_date_end', 'pub_date')
    list_filter = ['pub_date']

admin.site.register(Category)
admin.site.register(Event, EventAdmin)
admin.site.register(Place)
