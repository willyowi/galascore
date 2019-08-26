from django.db import models
import datetime as dt

# Create your models here.
class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length =10,blank = True)


    # querrying the database
    def __str__(self):
        return self.first_name


    #  save the messages
    def save_editor(self):
        self.save() 

    class Meta:
        ordering = ['first_name']


class tags(models.Model):
    name = models.CharField(max_length =30)


    def __str__(self):
        return self.name
                  