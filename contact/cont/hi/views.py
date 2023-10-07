from django.shortcuts import render
from hi.models import Contact

def contact(request):
    if request.method=="POST":
        print(request)
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        # contact = request.POST['contact']
        message = request.POST['message']
        print(fname, lname, email, message)
        contact=Contact(fname=fname,lname=lname,email=email,message=message)
        contact.save()
        
    return render(request,'contact.html')
