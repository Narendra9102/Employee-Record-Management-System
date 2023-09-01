from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('',views.index,name='index'),
    path('registration/',views.registration,name='registration'),
    path('user_login/',views.user_login,name='user_login'),
    path('emp_home/',views.emp_home,name='emp_home'),
    path('profile/',views.profile,name='profile'),
    path('logout/',views.Logout,name='logout'),
    path('admin_login/',views.admin_login,name='admin_login'),
    path('change_password/', views.change_password, name='change_password'),
    path('admin_home/',views.admin_home,name='admin_home'),
    path('change_passwordadmin/', views.change_passwordadmin, name='change_passwordadmin'),
    path('all_employee/', views.all_employee, name='all_employee'),
    path('chating/', views.chating, name='chating'),
    path('file_share/', views.file_share, name='file_share'),

]

urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)