import calendar
from datetime import date, datetime

from django.db.models import Sum
from django.shortcuts import render, get_object_or_404, redirect

from .forms import PlanForm, InitiativeForm, TacticForm
from .models import Offer, Plan, Initiative, Tactic, PLAN_STATUS_CHOICES


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


def plan_list(request):
    plans = Plan.objects.order_by("-created_at")

    # Search filter
    search_query = request.GET.get("search", "").strip()
    if search_query:
        plans = plans.filter(name__icontains=search_query)

    # Status filter
    status_filter = request.GET.get("status", "").strip()
    if status_filter:
        plans = plans.filter(status=status_filter)

    context = {
        "plans": plans,
        "search_query": search_query,
        "status_filter": status_filter,
        "status_choices": PLAN_STATUS_CHOICES,
    }
    return render(request, "marketing/plan_list.html", context)


def plan_create(request):
    if request.method == "POST":
        form = PlanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("marketing:plan_list")
    else:
        form = PlanForm()

    return render(request, "marketing/plan_form.html", {"form": form})


def plan_update(request, pk):
    plan = get_object_or_404(Plan, pk=pk)
    if request.method == "POST":
        form = PlanForm(request.POST, instance=plan)
        if form.is_valid():
            form.save()
            return redirect("marketing:plan_detail", pk=plan.pk)
    else:
        form = PlanForm(instance=plan)
    return render(request, "marketing/plan_form.html", {"form": form, "form_title": "Edit Plan"})


def plan_detail(request, pk):
    plan = get_object_or_404(Plan, pk=pk)
    tab = request.GET.get("tab", "overview")
    initiatives = plan.initiatives.order_by("-created_at")
    tactics = Tactic.objects.filter(initiative__plan=plan).order_by("-created_at")

    totals = initiatives.aggregate(
        planned_total=Sum("planned_amount"),
        actual_total=Sum("actual_amount"),
    )
    planned_total = totals["planned_total"] or 0
    actual_total = totals["actual_total"] or 0

    calendar_weeks = []
    calendar_month = None
    day_tactics = {}
    if tab == "calendar":
        month_param = request.GET.get("month")
        if month_param:
            try:
                calendar_month = datetime.strptime(month_param, "%Y-%m").date()
            except ValueError:
                calendar_month = date.today().replace(day=1)
        else:
            calendar_month = date.today().replace(day=1)

        cal = calendar.Calendar(firstweekday=6)
        calendar_weeks = cal.monthdatescalendar(calendar_month.year, calendar_month.month)

        for tactic in tactics:
            if not tactic.start_date or not tactic.end_date:
                continue
            start = tactic.start_date
            end = tactic.end_date
            for week in calendar_weeks:
                for day in week:
                    if start <= day <= end:
                        day_tactics.setdefault(day, []).append(tactic)

    context = {
        "plan": plan,
        "tab": tab,
        "initiatives": initiatives,
        "tactics": tactics,
        "planned_total": planned_total,
        "actual_total": actual_total,
        "variance_total": planned_total - actual_total,
        "calendar_month": calendar_month,
        "calendar_weeks": calendar_weeks,
        "day_tactics": day_tactics,
    }
    return render(request, "marketing/plan_detail.html", context)


def initiative_create(request, plan_id=None):
    initial = {}
    if plan_id:
        initial["plan"] = get_object_or_404(Plan, pk=plan_id)

    if request.method == "POST":
        form = InitiativeForm(request.POST)
        if form.is_valid():
            initiative = form.save()
            return redirect("marketing:plan_detail", pk=initiative.plan.pk)
    else:
        form = InitiativeForm(initial=initial)

    return render(
        request,
        "marketing/initiative_form.html",
        {"form": form, "form_title": "Create Initiative"},
    )


def initiative_update(request, pk):
    initiative = get_object_or_404(Initiative, pk=pk)
    if request.method == "POST":
        form = InitiativeForm(request.POST, instance=initiative)
        if form.is_valid():
            form.save()
            return redirect("marketing:plan_detail", pk=initiative.plan.pk)
    else:
        form = InitiativeForm(instance=initiative)

    return render(
        request,
        "marketing/initiative_form.html",
        {"form": form, "form_title": "Edit Initiative"},
    )


def initiative_delete(request, pk):
    initiative = get_object_or_404(Initiative, pk=pk)
    plan_id = initiative.plan.pk
    if request.method == "POST":
        initiative.delete()
        return redirect("marketing:plan_detail", pk=plan_id)

    return render(
        request,
        "marketing/confirm_delete.html",
        {
            "object_name": initiative.name,
            "cancel_url": "marketing:plan_detail",
            "cancel_kwargs": {"pk": plan_id},
        },
    )


def tactic_create(request, initiative_id=None):
    initial = {}
    if initiative_id:
        initial["initiative"] = get_object_or_404(Initiative, pk=initiative_id)

    if request.method == "POST":
        form = TacticForm(request.POST)
        if form.is_valid():
            tactic = form.save()
            return redirect("marketing:plan_detail", pk=tactic.initiative.plan.pk)
    else:
        form = TacticForm(initial=initial)

    return render(
        request,
        "marketing/tactic_form.html",
        {"form": form, "form_title": "Create Tactic"},
    )


def tactic_update(request, pk):
    tactic = get_object_or_404(Tactic, pk=pk)
    if request.method == "POST":
        form = TacticForm(request.POST, instance=tactic)
        if form.is_valid():
            form.save()
            return redirect("marketing:plan_detail", pk=tactic.initiative.plan.pk)
    else:
        form = TacticForm(instance=tactic)

    return render(
        request,
        "marketing/tactic_form.html",
        {"form": form, "form_title": "Edit Tactic"},
    )


def tactic_delete(request, pk):
    tactic = get_object_or_404(Tactic, pk=pk)
    plan_id = tactic.initiative.plan.pk
    if request.method == "POST":
        tactic.delete()
        return redirect("marketing:plan_detail", pk=plan_id)

    return render(
        request,
        "marketing/confirm_delete.html",
        {
            "object_name": tactic.name,
            "cancel_url": "marketing:plan_detail",
            "cancel_kwargs": {"pk": plan_id},
        },
    )
