from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from . import views
from django.http import HttpResponse

router = routers.DefaultRouter()


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'', views.list),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]