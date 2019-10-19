from django.db import models
import datetime
from django.utils import timezone

class Publisher(models.Model):
    article_address = models.URLField()
    date_submitted = models.DateTimeField('Date Submitted', auto_now_add=True)
    #date_submitted = models.DateTimeField('Date Submitted')
    def __str__(self):
        return self.article_address

## migrations are how we tell the app we changed our models
## makemigrations are how we do that
## 1. Change your models (in models.py).
## 2. Run python manage.py makemigrations to create migrations for those changes
## 3. Run python manage.py migrate to apply those changes to the database.

class Choice(models.Model):
    article = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    def __str__(self):
        return self.choice_text