
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    # path('about',views.about,name='about'),
    # path('projectpage',views.projectpage,name='projectpage'),
    # path('contactus',views.contact,name='contact'),
    # path('cvpage',views.cvpage,name='cvpage'),
    # path('saved',views.save_data,name='saveEq')
    

    
   
]
