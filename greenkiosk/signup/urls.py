from django.urls import path;
from .views import update_account


urlpatterns=[
path("customer/sign_in/",update_account,name="update_account"),

]