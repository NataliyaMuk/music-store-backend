from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Instruments)

admin.site.register(Category)

admin.site.register(Subcategory)

admin.site.register(Img_for_instrument)