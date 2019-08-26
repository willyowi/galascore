from django.conf.urls import url
from . import views


urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    

    url(r'^pics/',views.pic_today,name='picToday')
    # url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_news,name = 'pastNews'),
    #url(r'^search/', views.search_results, name='search_results'),
    #url(r'^article/(\d+)',views.article,name ='article')

]