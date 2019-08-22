from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
import datetime as dt


# Create your views here.

def pic_today(request):
    date = dt.date.today()
    # news = Article.todays_news()
     return render(request, 'all-news/today-news.html', {"date": date,"news":news}) 