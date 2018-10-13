from django.urls import path
from .views import storelist
# from Store.views import storelist

urlpatterns = [
    path('',storelist,name='storelist'),
]
