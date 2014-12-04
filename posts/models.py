from django.db import models

class Post(models.Model):
    title_text = models.CharField(max_length=32)
    pub_date = models.DateTimeField(auto_now_add=True, blank=True)
    def __unicode__(self):              # __unicode__ on Python 2
        return self.title_text

class Category(models.Model):
    name_text = models.CharField(max_length=32, unique=True)
    description_text = models.CharField(max_length=32, null=True)
    def clean_name_text(self):
        return self.cleaned_data["name_text"].lower()
    def __unicode__(self):              # __unicode__ on Python 2
        return self.name_text

class Event(Post):
    category = models.ForeignKey(Category)
    event_date_begin = models.DateTimeField('event date begin')
    event_date_end = models.DateTimeField('event date end')
    location_text = models.CharField(max_length=128, null=True)
    description_text = models.TextField(max_length=256, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

class Place(Post):
    place_date_begin = models.DateTimeField('place date begin')
    place_date_end = models.DateTimeField('place date end')
    location_text = models.CharField(max_length=128, null=True)
    description_text = models.TextField(max_length=256, null=True)
    price_range = models.IntegerField(default=0)


class Ad(Post):
    ad_date_begin = models.DateTimeField('ad date begin')
    ad_date_end = models.DateTimeField('ad date end')
    url = models.URLField(max_length=1000)
