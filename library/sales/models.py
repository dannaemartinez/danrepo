from enum import unique
from django.db import models
from library.books.models import Book
from library.clients.models import Client

# Create your models here.
class Sale(models.Model):
	client = models.ForeignKey(Client, related_name='SaleWithClient',on_delete=models.DO_NOTHING)
	total = models.DecimalField(max_digits = 6, decimal_places = 2, default= 0)
	books = models.ManyToManyField(Book, through='Article')
	def __str__(self) -> str:
		return "Sale ("+self.id.__str__()+"): client - "+ self.client.__str__()

class Article(models.Model):
	book = models.ForeignKey(Book, related_name='ArticlesWithBook', on_delete=models.DO_NOTHING)
	sale = models.ForeignKey(Sale, related_name='ArticleWithSale', on_delete=models.DO_NOTHING)
	quantity = models.SmallIntegerField()
	
	class Meta:
		unique_together = (("book","sale"),)