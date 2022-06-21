from django.urls import path
from . import views

urlpatterns = [
    path('', views.order, name="order"),
    # path("gallery", views.gallery, name="gallery"),
    path('view_orders', views.view_orders, name="view_orders"),
]

