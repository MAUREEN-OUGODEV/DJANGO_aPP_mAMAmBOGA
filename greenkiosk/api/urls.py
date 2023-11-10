from django.urls import path
from .views import CustomerListView, CustomerDetailView



urlpatterns =[
    path("customer/",CustomerListView.as_view(),name="customer_list_view"),
    path("customer/<int:id>/",CustomerDetailView.as_view(),name="customer_detail_view"),
    # path("add_to_cart/",AddToCartViews_as_view(),name="add_to_cart"),
]