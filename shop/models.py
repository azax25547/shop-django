from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):

    name = models.CharField(max_length=255, db_index=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Product(models.Model):

    name = models.CharField(max_length=255, db_index=True)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=9)
    rating = models.IntegerField()
    slug = models.SlugField(max_length=25, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_available = models.BooleanField(default=False)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name='products')

    class Meta:
        ordering = ('name',)
        index_together = (('id','slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail',args=[
            self.slug
        ])

