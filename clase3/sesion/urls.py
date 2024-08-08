from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name='home'),
    path("login/",views.user_login, name='login'),
    path("singup/",views.user_signup, name='signup'),
    path("logout/",views.user_logout, name='logout'),
    path('delete/',views.delete_user, name='delete')
]