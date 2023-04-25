from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Категории"
        verbose_name_plural = "Категории"


class Subcategory(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Подкатегории"
        verbose_name_plural = "Подкатегории"


class Img_for_instrument(models.Model):
    instrument_id = models.ForeignKey('Instruments', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True)

    def __str__(self):
        return str(self.instrument_id)
    
    class Meta:
        verbose_name = "Фотографии муз инструментов"
        verbose_name_plural = "Фотографии муз инстр"


class Instruments(models.Model):
    article = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    characteristics = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Муз инструменты"
        verbose_name_plural = "Муз инструменты"
        ordering = ['name']
