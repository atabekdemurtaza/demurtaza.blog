from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from .views import registration_view, logout_view


urlpatterns = [
    path(route='login/', view=obtain_auth_token, name='login'),
    path(route='logout/', view=logout_view, name='logout'),
    path(route='register/', view=registration_view, name='register'),
]
