from rest_framework import serializers
from .models import *

class SaleSerializer(serializers.ModelSerializer):
	books = serializers.StringRelatedField(many=True, read_only=True)
	class Meta:
		model = Sale
		fields = ['id', 'client', 'total', 'books']

class ArticleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Article
		fields = ['id', 'book', 'sale', 'quantity']
        