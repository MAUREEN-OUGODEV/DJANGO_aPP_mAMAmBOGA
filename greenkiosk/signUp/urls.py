from django.urls import path;
from .views import vendor_account


urlpatterns=[
path("vendor/sign_in/",vendor_account,name="vendor_account"),
]