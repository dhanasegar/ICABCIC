# urls.py
from django.urls import path
from . import views
from .views import home, paper, contact, contact_success, paper_success
urlpatterns = [
    path('', views.home, name='home'),  # Use function-based view
    path('paper/', views.paper, name='paper'),
    path('contact/', views.contact, name='contact'),
    path('contact/success/', contact_success, name='contact_success'), 
    path('paper/success/', paper_success, name='paper_success'),  

]

