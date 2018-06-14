from .views import add_book  
from django.conf.urls import url  



   
urlpatterns = [
    url(r'^add', add_book, name="add_book"),
]