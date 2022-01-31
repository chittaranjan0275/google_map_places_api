from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


from myapp.models import UserProfile


def landing(request):
    return render(request, 'landing/landing.html')  # landing page


def signin(request):
    if request.method == "GET":
        return render(request, 'landing/signin.html')  # redirect to signin page
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:  # sign in if it is already user else redirect to signup page
            login(request, user)
            return HttpResponseRedirect("/home")
        else:
            return render(request, 'landing/signup.html')


def signup(request):
    if request.method == "GET":
        return render(request, 'landing/signup.html')  # redirect to signup page
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=email).exists():
            return render(request, 'landing/signin.html')  # if user already exists redirect to signin page
        else:
            user = User.objects.create(username=email, email=email, first_name=first_name, last_name=last_name)
            user.set_password(password)
            user.save()
            user_profile = UserProfile.objects.create(user=user, email=email, first_name=first_name,
                                                      last_name=last_name)  # dob=dob, gender=gender)
            user_profile.save()  # save user data
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect("/home")  # Redirect to a success page.
            else:
                return HttpResponse("error")


def add_address(request):
    if request.method == "POST":
        print(request.method)
        print(request.POST)
        location = request.POST['location']
        landmark = request.POST['landmark']
        locality = request.POST['locality']
        administrative_area_level_1 = request.POST['administrative_area_level_1']
        postal_code = request.POST['postal_code']
        country = request.POST['country']
        latitude = request.POST['lat']
        longitude = request.POST['lng']
        user = request.user
        user_profile = UserProfile.objects.get(user=user)
        user_profile.location = location
        user_profile.landmark = landmark
        user_profile.locality = locality
        user_profile.administrative_area_level_1 = administrative_area_level_1
        user_profile.postal_code = postal_code
        user_profile.country = country
        user_profile.latitude = latitude
        user_profile.longitude = longitude
        user_profile.save()
        return render(request, 'landing/index.html')


def show_data(request):
    if request.method == 'POST':
        print(request.method)
        print(request.POST)
        locality = request.POST['locality']
        context = {}
        context["user_table"] = UserProfile.objects.filter(locality=locality)
        return render(request, 'landing/show_data.html', context)


def search_in_db(request):
    return render(request, 'landing/show_data.html')


@login_required(login_url="/signin")  # login require for welcome page
def index(request):
    return render(request, 'landing/index.html')
