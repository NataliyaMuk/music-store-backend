from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from import_export.admin import ExportActionMixin

# Register your models here.

from .models import *


class SubcategoryInline(ExportActionMixin, admin.TabularInline):
    model = Subcategory
    extra = 0


class ImgForInstrumentInline(ExportActionMixin, admin.TabularInline):
    model = Img_for_instrument
    extra = 0


class InstrumentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Instruments._meta.fields
                    if field.name not in ['description', 'characteristics']]
    inlines = [ImgForInstrumentInline]
    search_fields = ['name']
    list_filter = ('category', 'subcategory')
    ordering = ('id', 'price',)

    class Meta:
        model = Instruments


class CategoryAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = [field.name for field in Category._meta.fields]
    inlines = [SubcategoryInline]

    class Meta:
        model = Category


class SubcategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Subcategory._meta.fields]

    class Meta:
        model = Subcategory


class ImgForInstrumentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Img_for_instrument._meta.fields]

    class Meta:
        model = Img_for_instrument


class BlogAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Blog._meta.fields
                    if field.name not in ['description']]

    class Meta:
        model = Blog


admin.site.register(Instruments, InstrumentAdmin)

admin.site.register(Category, CategoryAdmin)

admin.site.register(Subcategory, SubcategoryAdmin)

admin.site.register(Img_for_instrument, ImgForInstrumentAdmin)

admin.site.register(Blog, BlogAdmin)
