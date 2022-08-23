"""django_tsst1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from pages.views import home_view, about_view, threed_model_view, \
    button, get_hand, video_stream, hand_control, mediapipe_view


# 此為向url提出有沒有符合的頁面，有的話就連過去
urlpatterns = [
    path('products/', include('products.urls')),
    path('partners/', include('partners.urls')),

    path('', home_view, name='home'),
    # path('home/', home_view),
    path('admin/', admin.site.urls),
    path('about/', about_view),
    path("3dtest/", threed_model_view),
    path("GetHand/", button),
    path("GetHand/getting", get_hand, name='get_your_hand'),
    path("GetHand/get_and_control", hand_control, name='get_hand_and_control'),
    path("GetHand_output/video_stream", video_stream),
    path("GetHand_output/mediapipe", mediapipe_view)
]
