from.import views
from django.urls import path

app_name = 'store_app'
urlpatterns = [
    path('',views.demo,name='demo'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('logout',views.logout,name='logout')


]