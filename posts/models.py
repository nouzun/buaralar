from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from easy_thumbnails.files import get_thumbnailer
from ajaximage.fields import AjaxImageField
import datetime

class Post(models.Model):
    title_text = models.CharField(max_length=32)
    user = models.ForeignKey(User, null=True)
    pub_date = models.DateTimeField(auto_now_add=True, blank=True)
    def __unicode__(self):              # __unicode__ on Python 2
        return self.title_text

class Category(models.Model):
    name_text = models.CharField(max_length=32, unique=True)
    description_text = models.CharField(max_length=32, null=True)
    def save(self, force_insert=False, force_update=False):
        self.name_text = self.name_text.lower()
        super(Category, self).save(force_insert, force_update)
    def __unicode__(self):              # __unicode__ on Python 2
        return self.name_text

class Event(Post):
    image = AjaxImageField(upload_to='thumbnails', thumbnail_width=605, thumbnail_height=150)
                               #max_height=200, #optional
                               #max_width=200, # optional
                               #crop=True # optional
    category = models.ForeignKey(Category)
    event_date_begin = models.DateTimeField('event date begin')
    event_date_end = models.DateTimeField('event date end')
    location_text = models.CharField(max_length=96, null=True)
    description_text = models.TextField(max_length=256, null=True)
    price_low = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    price_high = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    @property
    def get_date(self):
        event_day = None
        today = datetime.date.today()
        tomorrow = (datetime.date.today() + datetime.timedelta(days=1))
        third_day = (datetime.date.today() + datetime.timedelta(days=2))
        forth_day = (datetime.date.today() + datetime.timedelta(days=3))
        try:
            if (self.event_date_begin.date() >= today) & (self.event_date_begin.date() < tomorrow):
                event_day = "today"
            elif (self.event_date_begin.date() >= tomorrow) & (self.event_date_begin.date() < third_day):
                event_day = "tomorrow"
            elif (self.event_date_begin.date() >= third_day) & (self.event_date_begin.date() < forth_day):
                event_day = third_day.strftime("%A").lower()
        except Exception as e:
            print(e)
        return event_day

class Place(Post):
    CHEAP = '$'
    REASONABLE = '$$'
    EXPENSIVE = '$$$'
    OVERPRICED = '$$$$'
    PRICE_RANGE = (
        (CHEAP, 'Cheap'),
        (REASONABLE, 'Reasonable'),
        (EXPENSIVE, 'Expensive'),
        (OVERPRICED, 'Overpriced'),
    )
    place_date_begin = models.DateTimeField('place date begin')
    place_date_end = models.DateTimeField('place date end')
    location_text = models.CharField(max_length=96, null=True)
    description_text = models.TextField(max_length=256, null=True)
    price_range = models.CharField(max_length=4, choices=PRICE_RANGE, default=CHEAP)

class Ad(Post):
    ad_date_begin = models.DateTimeField('ad date begin')
    ad_date_end = models.DateTimeField('ad date end')
    url = models.URLField(max_length=1000)

@receiver(models.signals.post_delete, sender=Event)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.image:
        thumbmanager = get_thumbnailer(instance.image)
        thumbmanager.delete(save=False)
