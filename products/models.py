from django.db import models
from django.conf import settings
from django.shortcuts import reverse


CATEGORY_CHOICES = (
		('Fruits and Vegetables', 'Fruits and Vegetables'),
		('Electronics', 'Electronics'),
		('Clothing', 'Clothing'),
		('Books', 'Books'),
	)


class Item(models.Model):
	title = models.CharField(max_length=120)
	price = models.FloatField()
	discount_price = models.FloatField(blank=True, null=True)
	category = models.CharField(choices=CATEGORY_CHOICES, max_length=120, null=True, blank=True)
	image_url = models.CharField(max_length=2083, null=True, blank=True)
	slug = models.SlugField(null=True, blank=True)
	description = models.TextField(null=True, blank=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("product", kwargs={
			'slug': self.slug
		})

	def get_add_to_cart_url(self):
		return reverse("add-to-cart", kwargs={
			'slug': self.slug
		})

	def get_remove_from_cart_url(self):
		return reverse("remove-from-cart", kwargs={
			'slug': self.slug
		})


	class Meta:
	   ordering = ['-category']



class Variation(models.Model):
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	name = models.CharField(max_length=50, null=True, blank=True) # size, color

	class Meta:
		unique_together = (
			('item', 'name')
		)


	def __str__(self):
		return self.name


class ItemVariation(models.Model):
	variation  = models.ForeignKey(Variation, on_delete=models.CASCADE)
	value = models.CharField(max_length=50) # small, medium large etc


	class Meta:
		unique_together = (
			('variation', 'value')
		)

	def __str__(self):
		return self.value



VAR_CATEGORIES = (
    ('size', 'size',),
    ('color', 'color',),
)




# class VariationManager(models.Manager):
# 	def all(self):
# 		return super(VariationManager, self).filter(is_available=True)

# 	def sizes(self):
# 		return self.all().filter(variation_type='size')

# 	def colors(self):
# 		return self.all().filter(variation_type='color')

# VAR_TYPES = (
# 	('size', 'size'),
# 	('color', 'color')
# 	)

# class Variation(models.Model):
# 	item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True, blank=True)
# 	variation_type = models.CharField(max_length=120, choices=VAR_TYPES, default='Size')
# 	title = models.CharField(max_length=120, null=True, blank=True)
# 	price = models.FloatField(null=True, blank=True)
# 	is_available = models.BooleanField(default=True)

# 	objects = VariationManager()

# 	def __str__(self):
# 		return f"{self.item.title} {self.title}"