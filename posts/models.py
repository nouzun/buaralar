from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from easy_thumbnails.fields import ThumbnailerImageField
from easy_thumbnails.files import get_thumbnailer

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
    image = ThumbnailerImageField(upload_to='post_images', blank=True)
    category = models.ForeignKey(Category)
    event_date_begin = models.DateTimeField('event date begin')
    event_date_end = models.DateTimeField('event date end')
    location_text = models.CharField(max_length=128, null=True)
    description_text = models.TextField(max_length=256, null=True)
    price_low = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    price_high = models.DecimalField(max_digits=6, decimal_places=2, null=True)

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
    location_text = models.CharField(max_length=128, null=True)
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