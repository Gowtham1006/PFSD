from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = 'home'),
    path('sign-in/',views.signin, name = 'signin'),
    path('sign-up/',views.signup, name = 'signup'),
    path('profile/', views.profile, name='profile'),
    path('book/',views.book, name = 'book'),
    path('logout/', views.logoutPage, name='logout'),
    path('feedback/',views.feedback,name='feedback'),
path('filter-flights/', views.filter_flights, name='filter_flights'),
    path('ticket/',views.ticket,name='ticket'),
    path('clear/',views.clear,name='clear'),

]



