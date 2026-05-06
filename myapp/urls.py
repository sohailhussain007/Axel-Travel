from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('home', views.home, name="home"),
    path('about', views.about, name="about"),
    path('destinations', views.destinations, name="destinations"),
    path('gallery', views.gallery, name="gallery"),
    path('contact', views.contact, name="contact"),
    path('faq', views.faq, name="faq"),
    path('login', views.login, name="login"),
    path('signup', views.signup, name="signup"),
    path('logout', views.logout, name="logout"),
]
