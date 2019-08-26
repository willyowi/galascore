from django.db import models
import datetime as dt

# Create your models here.
class Postee(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length =10,blank = True)


    # querrying the database
    def __str__(self):
        return self.first_name


    #  save the messages
    def save_postee(self):
        self.save() 

    class Meta:
        ordering = ['first_name']


class tags(models.Model):
    name = models.CharField(max_length =30)


    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length= 40)

class Location(models.Model):
    name = models.CharField(max_length = 30) 
    def __str__(self):
        return self.name
         


class Image(models.Model):
    title = models.CharField(max_length =100)
    image = models.ImageField(upload_to = 'images/')
    details = models.TextField()
    postee = models.ForeignKey(Postee)
    location = models.ForeignKey(Location)
    category = models .ForeignKey(Category)

    #many to many r-ship= many images having many tags together
    tags = models.ManyToManyField(tags)

    #adding timestaps for dates for image
    pub_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    def save_Image(self):
        self.save()

    @classmethod 
    def today_images(cls):
        today=dt.date.today()
        galascore = cls.objects.filter(pub_date__date = today)
        return galascore

        


