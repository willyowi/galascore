from django.shortcuts import render
from django.http  import HttpResponse,Http404
import datetime as dt


# Create your views here.


def welcome(request):
    return render(request, 'welcome.html')

# def pic_today(request):
#     date = dt.date.today()
#     # news = Article.todays_news()
#      return render(request, 'all-news/today-news.html', {"date": date,"news":news}) 


# def convert_dates(dates):

#     # Function that gets the weekday number for the date.
#     day_number = dt.date.weekday(dates)

#     days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

#     # Returning the actual day of the week
#     day = days[day_number]
#     return day  
