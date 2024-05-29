from django.db import models

# Create your models here.
class Store(models.Model):
    RESTAURANT = "RESTAURANT"
    FASHION_STORE = "FASHION_STORE"
    ELECTRONICS_SHOP = "ELECTRONICS_SHOP"
    SUPERMARKET = "SUPERMARKET"
    VEGETABLE_FRUIT_SHOP = "VEGETABLE_FRUIT_SHOP"
    FISH_AND_MEAT = "FISH_AND_MEAT"
    OTHERS = "OTHERS"
    CATEGORY_CHOICES = (
        (RESTAURANT,RESTAURANT),
        (FASHION_STORE,FASHION_STORE),
        (ELECTRONICS_SHOP,ELECTRONICS_SHOP),
        (SUPERMARKET,SUPERMARKET),
        (VEGETABLE_FRUIT_SHOP,VEGETABLE_FRUIT_SHOP),
        (FISH_AND_MEAT,FISH_AND_MEAT),
        (OTHERS,OTHERS)
    )

    MODE_CHOICES = (
        ('OFFLINE','OFFLINE'),
        ('ONLINE','ONLINE'),
        ('BOTH','BOTH'),
    )
    store_name = models.CharField(max_length=100)
    desc = models.TextField(null=True,blank=True,default='')
    location = models.CharField(max_length=150)
    cover = models.ImageField(upload_to='store',null=True,blank=True)
    is_approved = models.BooleanField(default=False)
    category = models.CharField(max_length=50,default='OTHERS',choices=CATEGORY_CHOICES)
    mode = models.CharField(max_length=10,default='OFFLINE',choices=MODE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.store_name)
