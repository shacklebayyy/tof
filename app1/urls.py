from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views
from .views import register
from .views import search_student
from .views import  verify_otp  # Import verify_otp


app_name = 'app1'

urlpatterns = [
    path('verify_otp/', verify_otp, name='verify_otp'),  # Add this
    path('', views.index, name="index"),
    path('insert', views.insertData, name="insertData"),
    path('update/<int:id>/', views.updateData, name="updateData"),
    path('delete/<int:id>/', views.deleteData, name="deleteData"),
    path('viewdata/', views.viewdata, name='viewdata'),
    path('search/', search_student, name='search_student'),
    # Auth URLs
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='app1:login'), name='logout'),
]

# Serve media files in DEBUG mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
