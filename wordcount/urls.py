
from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('countit/',views.count,name='count'),
    path('about/',views.about,name='about')
]
