from django.urls import path
from . import views

app_name = "marketing"

urlpatterns = [
    path("offers/", views.offer_list, name="offer_list"),
    path("offers/<int:pk>/", views.offer_detail, name="offer_detail"),
]
