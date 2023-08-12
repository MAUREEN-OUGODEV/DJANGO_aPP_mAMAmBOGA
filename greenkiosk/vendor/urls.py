from django.urls import path;
from .views import vendor_details_views


urlpatterns=[
path("vendor/upload/",vendor_details_views,name="customer_details_views"),
]