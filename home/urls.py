from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login', views.userLogin, name='login'),
    path('logout', views.userLogout, name='logout'),
    path('marks/', views.marks, name='marks'),
    path('timetable/', views.timeTable, name='timetable'),
    path('<int:pk>', views.timeTableDisplay, name='timetable'),
    path('<int:pk>', views.timeTableDisplay, name='timetable'),
    path('marksenter', views.marksEnter, name='marksenter'),
    path('marksdisplay', views.marksDisplay, name='marksdisplay')
]
