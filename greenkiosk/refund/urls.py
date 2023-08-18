from django.urls import path
from.views import refund_view


urlpatterns=[
path("refund/upload/",refund_view,name="refund_views"),

]