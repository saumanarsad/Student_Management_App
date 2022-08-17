from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register_request, name="register"),
    path('logout/', views.logout_request, name="logout"),
    path('login/',views.login_request,name="login"),
    path('home/', views.index, name='index'),
    path('add/', views.add,name='add'),
    path('add/addrecord/', views.addrecord, name="addrecord"),
    path('home/delete/<int:id>', views.delete, name='delete'),
    path('home/update/<int:id>',views.update,name='update'),
    path('home/update/updaterecord/<int:id>', views.updaterecord,name = "updaterecord")


]