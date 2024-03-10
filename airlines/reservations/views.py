from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Flight, FormData
# @login_required(login_url='signin')
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import SearchForm

def filter_flights(request):
    origin = request.GET.get('origin', '')
    destination = request.GET.get('destination', '')

    # Filter flights based on origin and destination
    filtered_flights = Flight.objects.filter(source__icontains=origin, destination__icontains=destination)

    # Build HTML for filtered flights
    flight_list_html = ''
    for flight in filtered_flights:
        flight_list_html += f'<li>{flight.flight_number} - {flight.source} to {flight.destination}</li>'

    return JsonResponse({'flight_list': flight_list_html})



def home(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book')
    else:
        form = SearchForm()
    return render(request, 'home.html', {'form': form})

def book(request):
    # Here you can render another form with the saved data
    # Retrieve saved data and pass it to the context
    form_data = FormData.objects.last()  # Assuming you only have one instance
    return render(request, 'book.html', {'form_data': form_data})

    return render(request,'Home.html')

@login_required
def profile(request):
    return render(request, 'Profile.html', {'user': request.user})


def signin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        print(username,pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Username And Password is Incorrect")

    return render(request,'Sign-in.html')
def signup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if(pass1!=pass2):
            return HttpResponse("Password and Confirm Password are not Same!!         Same Same But Different!!")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            # return redirect('profile')
            return HttpResponse("You have Successfully Registered...Welcome to our Airlines!!")

        print(uname,email,pass1,pass2)
    return render(request,'Sign-up.html')

def feedback(request):
    return render(request,'feedback.html')
def book(request):
    return render(request,'book.html')
def logoutPage(request):
    logout(request)
    return redirect('signin')
from .models import *

@login_required(login_url='singin')
def ticket(request):
    if request.method=="POST":
        from1=request.POST.get("from1")
        to=request.POST.get("to")
        Ticket.objects.create(from1=from1,to=to)
        ticket=Ticket.objects.all()
        return render(request,'book.html',{'ticket':ticket})
    return render(request,'home.html')

def clear(request):
    de=Ticket.objects.all()
    de.delete()
    return render(request,'payment.html')