from django.urls import path
from . import views

app_name = "marketing"

urlpatterns = [
    path("offers/", views.offer_list, name="offer_list"),
    path("offers/<int:pk>/", views.offer_detail, name="offer_detail"),
    path("plans/", views.plan_list, name="plan_list"),
    path("plans/new/", views.plan_create, name="plan_create"),
    path("plans/<int:pk>/", views.plan_detail, name="plan_detail"),
    path("plans/<int:pk>/edit/", views.plan_update, name="plan_update"),
    path("initiatives/new/<int:plan_id>/", views.initiative_create, name="initiative_create"),
    path("initiatives/<int:pk>/edit/", views.initiative_update, name="initiative_update"),
    path("initiatives/<int:pk>/delete/", views.initiative_delete, name="initiative_delete"),
    path("tactics/new/<int:initiative_id>/", views.tactic_create, name="tactic_create"),
    path("tactics/<int:pk>/edit/", views.tactic_update, name="tactic_update"),
    path("tactics/<int:pk>/delete/", views.tactic_delete, name="tactic_delete"),
]
