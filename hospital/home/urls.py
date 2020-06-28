from django.urls import path,include
from .import views

urlpatterns = [
    path('', views.Index, name='home'),
    path('contact/', views.Contact, name='contact'),
    path('admin_login/', views.Login, name='login'),
    path('dashbord/', views.Dashbord, name='dashbord'),
    path('logout/', views.Logout_admin, name='logout'),
    path('view_doctor/', views.View_Doctor, name='view_doctor'),
    path('add_doctor/', views.Add_Doctor, name='add_doctor'),
    path('delect_doctor(?P(<int:id>)', views.Delect_Doctor, name='delect_doctor'),
    path('view_patient/', views.View_Patient, name='view_patient'),
    path('add_patient/', views.Add_Patient, name='add_patient'),
    path('delect_patient(?P(<int:id>)', views.Delect_Patient, name='delect_patient'),
    path('view_appointment/', views.View_Appointment, name='view_appointment'),
    path('add_appointment/', views.Add_Appointment, name='add_appointment'),
    path('delect_appointment(?P(<int:id>)', views.Delect_Appointment, name='delect_appointment'),
]
