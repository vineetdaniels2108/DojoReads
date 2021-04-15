from django.db import models
from loginapp.models import *

# Create your models here.

class Books(models.Model):
    title = models.CharField(max_length=80)
    author = models.CharField(max_length=50)
    rating = models.IntegerField()
    uploaded_by = models.ForeignKey(User, related_name = 'user_uploaded', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)
    
class Reviews(models.Model):
    review = models.TextField()
    posted_by = models.ForeignKey(User, related_name='user_post', on_delete = models.CASCADE)
    book = models.ForeignKey(Books, related_name='book_reviews', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)