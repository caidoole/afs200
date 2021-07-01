from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.home, name="mainsite-home"), 
    path('signup/', views.signup.as_view(), name="mainsite-signup")
]