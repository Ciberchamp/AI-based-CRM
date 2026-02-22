from django.urls import path
from . import views

app_name = "marketing"

urlpatterns = [
    path("offers/", views.offer_list, name="offer_list"),
    path("offers/<int:pk>/", views.offer_detail, name="offer_detail"),
    path("offers/", views.offer_list, name="offer_list"),
    path("offers/new/", views.offer_create, name="offer_create"),
    path("offers/<int:pk>/", views.offer_detail, name="offer_detail"),
    path("offers/<int:pk>/edit/", views.offer_update, name="offer_update"),
    path("offers/<int:offer_pk>/treatments/new/", views.treatment_create, name="treatment_create"),
    path("treatments/<int:pk>/preview/", views.treatment_preview, name="treatment_preview"),
    # Leads
    path("leads/", views.lead_list, name="lead_list"),
    path("leads/new/", views.lead_create, name="lead_create"),
    path("leads/<int:pk>/", views.lead_detail, name="lead_detail"),
    path("leads/<int:pk>/edit/", views.lead_update, name="lead_update"),
    path("leads/<int:pk>/delete/", views.lead_delete, name="lead_delete"),
    
    #------------------------------------
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
    
    # Campaigns
    path("campaigns/", views.campaign_list, name="campaign_list"),
    path("campaigns/new/", views.campaign_create, name="campaign_create"),
    path("campaigns/<int:pk>/", views.campaign_detail, name="campaign_detail"),
    path("campaigns/<int:pk>/edit/", views.campaign_update, name="campaign_update"),
    path("campaigns/<int:pk>/launch/", views.campaign_launch, name="campaign_launch"),
]
