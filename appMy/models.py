from django.db import models

# Create your models here.

class Blog(models.Model):
    title=models.CharField(("Başlık"),max_length=50)
    text=models.TextField()
    date_now=models.DateTimeField(("Tarih-Saat"), auto_now=False, auto_now_add=False)
    author=models.CharField(("Yazar"),max_length=50)