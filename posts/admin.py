from django.contrib import admin
from easy_thumbnails.widgets import ImageClearableFileInput
from posts.models import Post, Category, Event, Place, Ad
from easy_thumbnails.fields import ThumbnailerField

class EventInline(admin.TabularInline):
    model = Event

class EventAdmin(admin.ModelAdmin):
    formfield_overrides = {
            ThumbnailerField: {'widget': ImageClearableFileInput},
    }
    readonly_fields = ('user',)
    fieldsets = [
        ("Title",            {'fields': ['title_text']}),
        ('Image',            {'fields': ['image']}),
        ('Category',         {'fields': ['category']}),
        ('Description',      {'fields': ['description_text']}),
        ('Location',         {'fields': ['location_text']}),
        ('Price',            {'fields': ['price_low', 'price_high']}),
        ('Date',             {'fields': ['event_date_begin', 'event_date_end'], 'classes': ['']}),
    ]

    list_display = ('title_text', 'description_text', 'location_text', 'event_date_begin', 'event_date_end', 'user', 'pub_date')
    list_filter = ['pub_date']

    counted_fields = ('title_text', 'description_text', 'location_text')
    max_lengths = {'title_text': 32, 'description_text': 256, 'location_text': 128}

    class Media:
        js = ('http://code.jquery.com/jquery.min.js',
              'posts/js/jquery.charCount.js',)

    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super(EventAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        print db_field.name
        print self.counted_fields
        if db_field.name in self.counted_fields:
            try:
                len = self.max_lengths[db_field.name]
                field.widget.attrs['maxlength'] = len
            except: pass
            field.widget.attrs['class'] = 'counted ' + field.widget.attrs.get('class','')
        return field

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

class CategoryAdmin(admin.ModelAdmin):
    counted_fields = ('name_text', 'description_text')
    #really for textareas
    max_lengths = {'name_text': 32, 'description_text': 32}

    class Media:
        js = ('http://code.jquery.com/jquery.min.js',
              'posts/js/jquery.charCount.js',)

    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super(CategoryAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        print db_field.name
        print self.counted_fields
        if db_field.name in self.counted_fields:
            try:
                len = self.max_lengths[db_field.name]
                field.widget.attrs['maxlength'] = len
            except: pass
            field.widget.attrs['class'] = 'counted ' + field.widget.attrs.get('class','')
        return field

class PlaceAdmin(admin.ModelAdmin):
    readonly_fields = ('user',)
    fieldsets = [
        ("Title",            {'fields': ['title_text']}),
        ('Description',      {'fields': ['description_text']}),
        ('Location',         {'fields': ['location_text']}),
        ('Price',            {'fields': ['price_range']}),
        ('Date',             {'fields': ['place_date_begin', 'place_date_end'], 'classes': ['']}),
    ]

    list_display = ('title_text', 'description_text', 'location_text', 'price_range', 'place_date_begin', 'place_date_end', 'user', 'pub_date')
    list_filter = ['pub_date']

    counted_fields = ('title_text', 'description_text', 'location_text')
    max_lengths = {'title_text': 32, 'description_text': 256, 'location_text': 128}

    class Media:
        js = ('http://code.jquery.com/jquery.min.js',
              '/static/js/jquery.charCount.js',)

    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super(PlaceAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        print db_field.name
        print self.counted_fields
        if db_field.name in self.counted_fields:
            try:
                len = self.max_lengths[db_field.name]
                field.widget.attrs['maxlength'] = len
            except: pass
            field.widget.attrs['class'] = 'counted ' + field.widget.attrs.get('class','')
        return field

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()


admin.site.register(Category, CategoryAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Place, PlaceAdmin)
