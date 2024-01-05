from django.urls import path,include
from shop import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('feed', views.feedback, name = 'feedback'),
    path('about', views.about, name = 'feedback'),
    path('signup', views.signup, name = 'signup'),
    path('login', views.login_view, name = 'login'),
    path('loginUser', views.loginUser, name = 'login'),
    path('logout', views.logOut, name = 'logout'),
    path('map', views.map, name = 'map'),
    path('telangana', views.telangana, name = 'telangna'),
    path('andhra', views.andhra, name = 'andhra'),
    path('uttar', views.uttar, name = 'uttar'),
    path('maha', views.maha, name = 'maha'),
    path('raja', views.raja, name = 'raja'),
    # path('export', views.export_users_csv, name = 'export'),
]