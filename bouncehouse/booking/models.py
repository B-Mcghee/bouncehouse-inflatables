from django.db import models
from io import BytesIO
from PIL import Image as Pillow
from django.utils import timezone
from django.core.files import File
from django.db.models.fields import DateTimeField



class Collection(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    feature_image = models.ImageField(upload_to='features')

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}'

class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    price_per_day = models.DecimalField(max_digits=6, decimal_places=2)
    cover_image = models.ImageField(upload_to=f'images', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='images', blank=True, null=True)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering = ('-date_added', )

    def __str__(self):
        return self.name

    def get_absolute_url(self, collection_slug):
        return f'/{collection_slug}/{self.slug}/'

    def get_image(self):
        if self.cover_image:
            return 'http://127.0.0.1:8000' + self.cover_image.url
        return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.cover_image:
                self.thumbnail = self.make_thumbnail(self.cover_image)
                self.save()

                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''
    
    

    def make_thumbnail(self, image, size=(300, 200)):
        img = Pillow.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail


class Image(models.Model):
    file_name = models.CharField(max_length=255)
    bounce_house = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_images = models.ImageField(upload_to='images')


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=11)

class Reservation(models.Model):
    reserved_date = models.DateTimeField()
    days = models.IntegerField(1)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=5)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-reserved_date',)

class Booking(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    security_deposit = models.DecimalField(max_digits=5, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=5, decimal_places=2)
    