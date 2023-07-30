from django.urls import path
from restaurant import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homepage,name="homepage"),
    path('dashboard/', views.dashboard,name="dashboard"),
    path('registration/', views.registration,name="registration"),
    path('login/', views.login,name="login"),
    path('logout/', views.logout,name="logout"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
