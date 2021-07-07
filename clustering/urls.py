from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('', views.base, name="base"),
    path('home', views.home, name="home"),
    path('account/', views.accountSettings, name="account"),
    
    path('predict/', views.predict, name="predict"),
    path('predict/result', views.result, name="result"),

    path('customer/<str:pk>/', views.customer, name="customer"),
    path('data/', views.data, name="data"),

    path('create_data/', views.createData, name="create_data"),
    path('update_data/<str:pk>/', views.updateData, name="update_data"),
    path('delete_data/<str:pk>/', views.deleteData, name="delete_data"),

    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), 
        name="password_reset_complete"),
] 