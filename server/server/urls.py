"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url
from . import views,get_database_data
urlpatterns = [
    url(r'^$', views.index),
    url(r'^data/imagesData/$', views.image_page),
    url(r'^data/infraredData/$', views.infrared_page),
    url(r'^data/ultrasonicData/$', views.ultrasonic_page),
    url(r'^head/$', views.head),
    url(r'^left/$', views.left),
    url(r'^main/$', views.main),
    url(r'^foot/$', views.foot),
    url(r'^js/$', views.js),
    url(r'^data/getInfraredData/$', get_database_data.getInfraredData),
    url(r'^data/saveInfraredData/$', get_database_data.saveInfraredData),
    url(r'^data/updateInfraredData/$', get_database_data.updateInfraredData),
    url(r'^data/deleteInfraredData/$', get_database_data.deleteInfraredData),
    url(r'^data/getUltrasonicData/$', get_database_data.getUltrasonicData),
    url(r'^data/saveUltrasonicData/$', get_database_data.saveUltrasonicData),
    url(r'^data/updateUltrasonicData/$', get_database_data.updateUltrasonicData),
    url(r'^data/deleteUltrasonicData/$', get_database_data.deleteUltrasonicData),
    url(r'^data/getImagesData', get_database_data.getImagesData),
    url(r'^data/saveImagesData/$', get_database_data.saveImagesData),
    url(r'^data/updateImagesData/$', get_database_data.updateImagesData),
    url(r'^data/deleteImagesData/$', get_database_data.deleteImagesData)
]
