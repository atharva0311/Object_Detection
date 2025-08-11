# """
# URL configuration for Project project.

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/5.2/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin # type: ignore
# from django.urls import path # type: ignore
# from . import views
# from django.conf.urls.static import static #type:ignore
# from . import settings







from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('Features/', views.feature, name='image'),
    path('webcam/', views.webcam, name='webcam'),

    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    # Endpoint for streaming the webcam video with detections
    path('video_feed/', views.video_feed, name='video_feed'),


]
