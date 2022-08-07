from django.urls import path
from . import views
from .views import PasswordsChangeView


urlpatterns = [
    path("", views.home, name = "home"),
    path('logout',views.logoutpage , name='logout'),
    path("home", views.home, name = "index"),
    path('localisation', views.localisation, name = 'localisation'), 
    path('restaurant', views.restaurant, name = 'restaurant'), 
    path('hotel', views.hotel, name = 'hotel'), 
    path('attraction', views.attraction, name = 'attraction'), 

    path('restaurant_localisation', views.restaurant_localisation, name = 'restaurant_localisation'), 
    path('hotel_localisation', views.hotel_localisation, name = 'hotel_localisation'), 
    path('attraction_localisation', views.attraction_localisation, name = 'attraction_localisation'), 
    path('nearby_false', views.nearby_false, name='nearby_false'),   
    path('register',views.registerpage,name='register'),
    path('login',views.loginpage,name='login'),
    path('service/<int:id_service>',views.service,name='service'),
    path('profile',views.profile,name='profile'),
    path('favourite/',views.favourite,name='favourite'),
    path('wishlist/<int:id>',views.add_to_wishlist,name="wishlist"),
    path('password',PasswordsChangeView.as_view(template_name='index/password.html')),
    path('change-password-done/',views.password_success ,name='change-password-done'),
    #path('db',views.db,name='db')
]