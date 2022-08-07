from email import message
from django.shortcuts import render,redirect
from .models import Service
from .models import Image
from django.http import HttpResponse
from .forms import NameForm , Utilisateur , Up
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import login,logout,authenticate
from django.shortcuts import get_object_or_404
import pymysql
from django.http import JsonResponse, HttpResponse , HttpResponseRedirect
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy



# Create your views here.


def fav(request,id):
    post=Service.objects.filter(fav=id)
    if post.exists():
        post.fav.remove(id)
    else:
        post.fav.add(id)
    list_services = fetch_img()
    return render(request, "index/index2.html", {"liste_services":list_services})

    

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('profile.html')
def password_success(request):
      return render(request,'index/index2.html',{})


def registerpage(request):
    form=Utilisateur()
    if request.method =='POST':
        form=Utilisateur(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    
    
    context = {'form':form}
    return render(request, "index/register.html",context)


def loginpage(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            return redirect('home')
    
    
    return render(request, "index/login.html")


def fetch_img():
    list_services = Service.objects.all()
    for s in list_services:
        images = s.images.all()
        if images:
            s.thumbail = images[0].Web_adresse_Img
    return list_services


def fetch_loc(lat, long):
    lat_g = lat - 0.001
    long_g = long - 0.001
    lat_l = lat + 0.001
    long_l = long + 0.001
    list_services = Service.objects.raw('select * from Service where Latitude_Service >= %s and Longitude_Service >= %s and Latitude_Service <= %s and Longitude_Service <= %s', [lat_g,long_g,lat_l,long_l])
    for s in list_services:
        images = s.images.all()
        if images:
            s.thumbail = images[0].Web_adresse_Img
    return list_services
    

def home(request):
    if request.method == 'POST':
        formulaire = NameForm(request.POST)

        if not formulaire.is_valid():
            return render(request, "index/index.html", {message : "Form invalid"})

        lat = formulaire.cleaned_data['longitude']
        long = formulaire.cleaned_data['latitude']
        list_services = fetch_loc(lat, long)
        return render(request, "index/localisation.html", {"liste_services":list_services})
    else :
        list_services = fetch_img()
        return render(request, "index/index.html", {"liste_services":list_services})


def localisation(request):
    list_services = fetch_img()
    return render(request, "index/localisation.html", {"liste_services":list_services})


def hotel(request):
    if request.method == 'POST':
        formulaire = NameForm(request.POST)

        if not formulaire.is_valid():
            return render(request, "index/hotel.html", {message : "Form invalid"})

        lat = formulaire.cleaned_data['longitude']
        long = formulaire.cleaned_data['latitude']
        list_services = fetch_loc(lat, long)
        return render(request, "index/hotel_localisation.html", {"liste_services":list_services})
    else :
        list_services = fetch_img()
        return render(request, "index/hotel.html", {"liste_services":list_services})      

    

def restaurant(request):
    if request.method == 'POST':
        formulaire = NameForm(request.POST)

        if not formulaire.is_valid():
            return render(request, "index/hotel.html", {message : "Form invalid"})

        lat = formulaire.cleaned_data['longitude']
        long = formulaire.cleaned_data['latitude']
        list_services = fetch_loc(lat, long)
        return render(request, "index/hotel_localisation.html", {"liste_services":list_services})
    else :
        list_services = fetch_img()
        return render(request, "index/restaurant.html", {"liste_services":list_services})

def attraction(request):
    if request.method == 'POST':
        formulaire = NameForm(request.POST)

        if not formulaire.is_valid():
            return render(request, "index/hotel.html", {message : "Form invalid"})

        lat = formulaire.cleaned_data['longitude']
        long = formulaire.cleaned_data['latitude']
        list_services = fetch_loc(lat, long)
        return render(request, "index/hotel_localisation.html", {"liste_services":list_services})
    else :
        list_services = fetch_img()
        return render(request, "./index/attraction.html", {"liste_services":list_services})


def restaurant_localisation(request):
    list_services = fetch_img()
    return render(request, "./index/restaurant_localisation.html", {"liste_services":list_services})


def hotel_localisation(request):
    list_services = fetch_img()
    return render(request, "./index/hotel_localisation.html", {"liste_services":list_services})


def attraction_localisation(request):
    list_services = fetch_img()
    return render(request, "./index/attraction_localisation.html", {"liste_services":list_services})


def imgs(id_service):
    list_services = Service.objects.filter(id = id_service)
    for s in list_services:
        images = s.images.all()
        for i in images :
            i.Nom_Service = s.Nom_Service
            i.Longitude_Service = s.Longitude_Service
            i.Latitude_Service = s.Latitude_Service
    return images

def service(request,id_service):
    nb = 1
    images = imgs(id_service)
    for i in images:
        i.nbr = nb
        nb = nb+1
    return render(request,"./index/service.html",{"images":images})



def logoutpage(request):
    logout(request)
    return redirect('index')



def db(request):

    services_str = "6415331,33.5798,-7.55964,Crazy Park,attraction\n15153598,33.594166,-7.59951,Kyriad Residence Casablanca Centre Ville,hotel\n18543404,33.58834,-7.5644,Sushi d'or,restaurant\n20302227,33.58734,-7.54686,Bab el Marsa,attraction\n14111085,33.5935,-7.59954,Hotel Campanile Casablanca Centre Ville,hotel\n10688034,33.59235,-7.56528,Sun7,restaurant\n"
    images_str_lines = images_str.split("\n")
    
    services = []
    images = []

    for line in services_str_lines[1:]:
        service_line = line.split(",")
        if len(service_line) > 1:
            row_dict = {
                "service_id" : service_line[0],
                "latitude" : service_line[1],
                "longitude" : service_line[2],
                "title" : service_line[3],
                "type" : service_line[4].strip(),
            }
            services.append(row_dict)

    for line in images_str_lines[1:]:
        image_line = line.split(",")
        if len(image_line) > 1:
            row_dict = {
                "service_id" : image_line[0],
                "url" : image_line[1],
            }
            images.append(row_dict)

    for service in services:
        service["images"] = []
        for image in images:
            if service["service_id"] == image["service_id"]:
                service["images"].append(image["url"])

    # if this loop got you duplicate key errors comment it and uncommrnt the next 2 commented loops
    for service in services:
        s = Service(Latitude_Service=float(service["latitude"]), Longitude_Service=float(service['longitude']), Nom_Service=service["title"], Type_Service=service["type"])
        s.save()
        for image in service["images"]:
            i = Image(Web_adresse_Img = image, service = s)
            i.save()


    return HttpResponse("done lmlaaaaawi")
    
    
    
def nearby_false(request):
        list_services = fetch_img()
        item_name = request.GET.get('item-name')
        if item_name !='' and item_name is not None:
            list_services = Service.objects.filter(Nom_Service__icontains=item_name)
            for s in list_services:
                images = s.images.all()
                if images:
                    s.thumbail = images[0].Web_adresse_Img        
        return render(request, "index/search.html", {"liste_services": list_services})
    
    
def profile1(request):
    user_form = UpdateUserForm(instance=request.user)
    profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'index/profile.html', {'user_form': user_form, 'profile_form': profile_form})





def profile(request):
    if request.method == 'POST':
        u_form = Up(request.POST,instance=request.user)
        if u_form.is_valid():
            u_form.save()
            return redirect('profile')
    else:
        u_form = Up(instance=request.user)

    context = {'u_form':u_form}
    return render(request, 'index/profile.html', context)


   
    
    






def add_to_wishlist(request,id):
    service = get_object_or_404(Service, id=id)
    if service.users_wishlist.filter(id=request.user.id).exists():
        service.users_wishlist.remove(request.user)
    else:
        service.users_wishlist.add(request.user)
    return HttpResponseRedirect(request.META["HTTP_REFERER"])





def favourite(request):
    new = Service.objects.filter(users_wishlist=request.user)
    for s in new:
        images = s.images.all()
        if images:
            s.thumbail = images[0].Web_adresse_Img
    return render(request,'index/wishlist.html',{"favourite": new})