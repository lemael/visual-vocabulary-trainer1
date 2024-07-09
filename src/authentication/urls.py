from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path

from authentication import views

urlpatterns=[
  path('home/', views.home, name='home'),
  path('login/',auth_views.LoginView.as_view(template_name="app/login.html"),name='login'),
  path('logout',auth_views.LogoutView.as_view(template_name="app/index.html"),name='logout'),
  path('register',views.register,name='register'),
  path('activate/<uidb64>/<token>', views.activate, name="activate")
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

