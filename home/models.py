from django.db import models

# Create your models here.


class Category(models.Model):
    category_name=models.CharField(max_length=150)


    def __str__(self):
        return self.category_name

class Book(models.Model):
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    book_title=models.CharField(max_length=150)

    def __str__(self):
        return self.book_title





class Student(models.Model):
    name=models.CharField(max_length=150)
    age=models.IntegerField(default=18)
    father_name=models.CharField(max_length=150)


    def __str__(self):
        return self.name