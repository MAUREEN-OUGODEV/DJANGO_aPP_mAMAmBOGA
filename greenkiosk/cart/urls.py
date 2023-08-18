from .views import cart_upload_form,cart_list,cart_detail,edit_cart_view
from django.urls import path

urlpatterns=[
    path('cart/upload/', cart_upload_form, name='cart_upload_view'),
    path('cart/list/', cart_list, name='cart_list_view'),
    path("cart/<int:id>/",cart_detail,name="cart_detail_view"),
    path("cart/edit/<int:id>/", edit_cart_view, name="cart_edit_view")
]