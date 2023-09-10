from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=100) 
    n_pages = models.IntegerField()

    in_house = models.BooleanField(default=True)
    floor = models.IntegerField(default=0)
    shelf = models.IntegerField(default=0)

    retired_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.author}"

class Transaction(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    returned = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if (self.returned):
            return f"{self.user} returned {self.book}."
        else:
            return f"{self.user} got {self.book}."