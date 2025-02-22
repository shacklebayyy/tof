from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views
from .views import register

app_name = 'app1'

urlpatterns = [
    path('', views.index, name="index"),
    path('insert', views.insertData, name="insertData"),
    path('update/<int:id>/', views.updateData, name="updateData"),
    path('delete/<int:id>/', views.deleteData, name="deleteData"),
    path('viewdata/', views.viewdata, name='viewdata'),

    # Auth URLs
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]

# Serve media files in DEBUG mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
