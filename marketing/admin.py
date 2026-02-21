from django.contrib import admin
from .models import Offer, Treatment


class TreatmentInline(admin.TabularInline):
    model = Treatment
    extra = 1


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active", "created_at")
    list_filter = ("is_active",)
    search_fields = ("name", "description")
    inlines = [TreatmentInline]


@admin.register(Treatment)
class TreatmentAdmin(admin.ModelAdmin):
    list_display = ("name", "offer", "channel", "is_active", "created_at")
    list_filter = ("channel", "is_active")
    search_fields = ("name", "subject", "body")
