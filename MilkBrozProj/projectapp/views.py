from django.shortcuts import render

# Create your views here.
import datetime
from queue import Empty
from django.shortcuts import render
from projectapp.models import Contact
from django.contrib import messages
# Create your views here.       
def index(request):
   
    return render(request,'assest/index.html')



# def save_data(request):
    
#     if (request.method == 'POST'):
        
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         desc = request.POST.get('proj')
#         if len(name)<2 or len(email)<6 or len(desc)<3:
#             messages.error(request,'Please fill form correctly')
        

#         else:
#             data = Contact(name=name, email=email, desc=desc, date=datetime.datetime.now())
#             messages.success(request,'Thank you for reaching us.Your Response has been Recorded')
#             data.save()
        
#     return render(request,'projectapp/contact me.html')    

