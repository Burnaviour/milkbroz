
from django.shortcuts import render
import uuid
# Create your views here.
import datetime

from django.shortcuts import render
from projectapp.models import Contact
from django.contrib import messages
# Create your views here.       
def index(request):
   
    return render(request,'assests/index.html')

def gallery(request):
    
    
    # context = {'cos':'cash on delivery',
    #                            'cc':'Using visa card'
    #                            }
   

        
    return render(request,'assests/gallery.html') 
def shop(request):
    
    
    context = {'cos':'cash on delivery',
                               'cc':'Pickup'
                               }

        
    return render(request,'assests/shop.html',context) 
          
def about(request):
    
    
    # context = {'cos':'cash on delivery',
    #                            'cc':'Using visa card'
    #                            }
   

        
    return render(request,'assests/about.html') 
     

def save_data(request):
    context = {'cos':'cash on delivery',
                               'cc':'Pickup'
                               }
    if (request.method == 'POST'):
        test = uuid.uuid4()
        
        name = request.POST.get('name')
      
        answer = request.POST.get('answer')
        phonenumber = request.POST.get('quantity')
        address = request.POST.get('proj')
        if len(name)<2 or len(address)<15 or len(phonenumber)<8:
            messages.error(request,'Please fill form correctly')
        

        else:

            data = Contact(name=name, phone_number=phonenumber,address=address ,payment=answer, date=datetime.datetime.now(),trans_id=test)
            messages.success(request,'Your order has been placed.it will be delivered shortly.')
            data.save()
    return render(request,'assests/shop.html',context) 

