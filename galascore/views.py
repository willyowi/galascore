from django.shortcuts import render, redirect
from django.http  import HttpResponse,Http404
import datetime as dt


# Create your views here.


def welcome(request):
    return render(request, 'welcome.html')


def pic_today(request):
    date = dt.date.today()
    #news = Article.todays_news()
    return render(request, 'all-pics/today-pics.html', {"date": date}) 


def convert_dates(dates):

     # Function that gets the weekday number for the date.
     day_number = dt.date.weekday(dates)

     days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

     # Returning the actual day of the week
     day = days[day_number]
     return day  
