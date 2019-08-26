from django.shortcuts import render, redirect
from django.http  import HttpResponse,Http404
import datetime as dt
from .models import Image


# Create your views here.


def welcome(request):
    return render(request, 'welcome.html')


def pic_today(request):
    date = dt.date.today()
    galascore = Image.objects.all()
    return render(request, 'all-pics/today-pics.html', {"date": date,"galascore":galascore}) 


def convert_dates(dates):

     # Function that gets the weekday number for the date.
     day_number = dt.date.weekday(dates)

     days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

     # Returning the actual day of the week
     day = days[day_number]
     return day  

def image(request,image_id):
    try:
        article = Article.objects.get(id = article_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-news/image-details.html", {"image":image})