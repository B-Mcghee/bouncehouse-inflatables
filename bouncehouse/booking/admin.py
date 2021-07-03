from django.contrib import admin
from .models import Booking, Customer, Product, Collection, Reservation, Image

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_per_day')
    list_filter = ('name', 'price_per_day',)
    prepopulated_fields = {'slug': ('name',)}

class CollectionAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('name',)}

class ImageAdmin(admin.ModelAdmin):
    list_display = ('file_name', 'bounce_house')
    list_filter = ('bounce_house',)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('last_name',)
    list_filter = ('last_name',)

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('reserved_date',)
    list_filter = ('customer',)
      

admin.site.register(Collection, CollectionAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Booking)
admin.site.register(Reservation,ReservationAdmin)



