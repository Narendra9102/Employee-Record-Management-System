from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('',views.index,name='index'),
    path('registration/',views.registration,name='registration'),
    path('emp_login/',views.emp_login,name='emp_login'),
    path('emp_home/',views.emp_home,name='emp_home'),
    path('profile/',views.profile,name='profile'),
    path('logout/',views.Logout,name='logout'),
    path('admin_login/',views.admin_login,name='admin_login'),
    path('my_experience/',views.my_experience,name='my_experience'),
    path('edit_myexperience/',views.edit_myexperience,name='edit_myexperience'),
    path('my_education/', views.my_education, name='my_education'),
    path('edit_myeducation/', views.edit_myeducation, name='edit_myeducation'),
    path('change_password/', views.change_password, name='change_password'),
    path('admin_home/',views.admin_home,name='admin_home'),
    path('change_passwordadmin/', views.change_passwordadmin, name='change_passwordadmin'),
    path('all_employee/', views.all_employee, name='all_employee'),


]

urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)