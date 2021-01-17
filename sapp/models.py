from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class BookDetails(models.Model):
    bok = models.ForeignKey('Book', on_delete=models.CASCADE, related_name="rbook")
    summary = models.CharField(max_length=200) # one book can have multiple summaries