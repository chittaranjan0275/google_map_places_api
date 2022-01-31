from django.urls import path

from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('home/', views.index, name='index'),
    path('add_address/', views.add_address, name='add_address'),
    path('show_data/', views.show_data, name='show_data'),
    path('search_in_db/', views.search_in_db, name='search_in_db'),
]
