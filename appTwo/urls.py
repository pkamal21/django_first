from django.conf.urls import url
from appTwo import views

app_name = 'appTwo'

urlpatterns = [
    url(r'^users/',views.users,name='users'),
    url(r'^details/',views.details,name='details'),
]
