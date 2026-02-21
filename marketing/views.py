from django.shortcuts import render, get_object_or_404
from .models import Offer


def offer_list(request):
    offers = Offer.objects.filter(is_active=True).order_by("-created_at")
    context = {"offers": offers}
    return render(request, "marketing/offer_list.html", context)


def offer_detail(request, pk):
    offer = get_object_or_404(Offer, pk=pk)
    treatments = offer.treatments.filter(is_active=True).order_by("-created_at")
    context = {
        "offer": offer,
        "treatments": treatments,
    }
    return render(request, "marketing/offer_detail.html", context)
