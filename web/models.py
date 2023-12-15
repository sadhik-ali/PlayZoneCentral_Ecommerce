from django.db import models

# Create your models here.

class Category(models.Model):
  name = models.CharField(max_length=200)
  slug = models.SlugField(unique=True)
  display_in_home = models.BooleanField(default=False)

  def get_products(self):
    return Product.objects.filter(category=self)

  def __str__(self):
   return self.name
  
class Product(models.Model):
  category = models.ForeignKey('web.Category',verbose_name='Product Category',related_name='product_category',on_delete=models.CASCADE)
  image = models.ImageField(upload_to='media/',help_text='supporting fale....',blank=True,null=True)
  name = models.CharField(max_length=100)
  price = models.IntegerField()

  def __str__(self):
   return self.name
  
class LogoSectionProduct(models.Model):
  LogoImage = models.ImageField(upload_to='media')

