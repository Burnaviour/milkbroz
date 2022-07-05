
from django.urls import path
from django.contrib import admin

from . import views

admin.site.site_header = "Contact Admin"
admin.site.site_title = "Contact Admin Portal"
admin.site.index_title = "Welcome to Contact Portal"


urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('saved',views.save_data,name='saveEq'),
    path('gallery',views.gallery,name='gallery'),
    path('shop',views.shop ,name='shop')
    # path('projectpage',views.projectpage,name='projectpage'),
    # path('contactus',views.contact,name='contact'),
    # path('cvpage',views.cvpage,name='cvpage'),
    
    

    
   
]
