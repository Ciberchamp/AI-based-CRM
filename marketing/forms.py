from django import forms
from .models import Offer, Plan, Initiative, Tactic, PLAN_STATUS_CHOICES, Treatment, Lead, Campaign, CampaignResponse



class PlanForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        budget_field = self.fields.get("total_budget")
        if budget_field:
            budget_field.required = False
            # Clear initial value if it's 0 or if creating a new instance
            if not self.instance or not self.instance.pk or self.instance.total_budget == 0:
                budget_field.initial = None
            budget_field.widget.attrs.update({
                "placeholder": "Enter amount (optional)",
                "value": "" if (not self.instance or not self.instance.pk or self.instance.total_budget == 0) else self.instance.total_budget
            })

    class Meta:
        model = Plan
        fields = [
            "name",
            "description",
            "status",
            "start_date",
            "end_date",
            "total_budget",
        ]
        widgets = {
            "start_date": forms.DateInput(attrs={"type": "date"}),
            "end_date": forms.DateInput(attrs={"type": "date"}),
            "total_budget": forms.NumberInput(attrs={"placeholder": "Enter amount (optional)"}),
        }


class InitiativeForm(forms.ModelForm):
    class Meta:
        model = Initiative
        fields = [
            "plan",
            "name",
            "description",
            "status",
            "start_date",
            "end_date",
            "planned_amount",
            "actual_amount",
        ]
        widgets = {
            "start_date": forms.DateInput(attrs={"type": "date"}),
            "end_date": forms.DateInput(attrs={"type": "date"}),
        }


class TacticForm(forms.ModelForm):
    class Meta:
        model = Tactic
        fields = [
            "initiative",
            "name",
            "description",
            "status",
            "start_date",
            "end_date",
            "planned_amount",
            "actual_amount",
        ]
        widgets = {
            "start_date": forms.DateInput(attrs={"type": "date"}),
            "end_date": forms.DateInput(attrs={"type": "date"}),
        }


# no changes made above.. usha work below

class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ["name", "code", "description", "is_active"]
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Offer name",
            }),
            "code": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Offer code",
            }),
            "description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "Describe the proposition, eligibility, etc.",
            }),
            "is_active": forms.CheckboxInput(attrs={
                "class": "form-check-input",
            }),
        }


class TreatmentForm(forms.ModelForm):
    class Meta:
        model = Treatment
        fields = ["name", "channel", "subject", "body", "is_active"]
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Treatment name (e.g. Welcome Email v1)",
            }),
            "channel": forms.Select(attrs={
                "class": "form-select",
            }),
            "subject": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Subject line / title",
            }),
            "body": forms.Textarea(attrs={
                "class": "form-control font-monospace",
                "rows": 8,
                "placeholder": "Message body. You can use {{first_name}} etc.",
            }),
            "is_active": forms.CheckboxInput(attrs={
                "class": "form-check-input",
            }),
        }


#------------------- usha block starts -------------------
class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = [
            "first_name",
            "last_name",
            "job_title",
            "company",
            "industry",
            "company_size",
            "email",
            "phone",
            "city",
            "country",
            "status",
            "source",
            "rating",
            "owner",
            "offer",
            "notes",
        ]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "job_title": forms.TextInput(attrs={"class": "form-control"}),
            "company": forms.TextInput(attrs={"class": "form-control"}),
            "industry": forms.TextInput(attrs={"class": "form-control"}),
            "company_size": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "city": forms.TextInput(attrs={"class": "form-control"}),
            "country": forms.TextInput(attrs={"class": "form-control"}),
            "status": forms.Select(attrs={"class": "form-select"}),
            "source": forms.Select(attrs={"class": "form-select"}),
            "rating": forms.Select(attrs={"class": "form-select"}),
            "owner": forms.TextInput(attrs={"class": "form-control"}),
            "offer": forms.Select(attrs={"class": "form-select"}),
            "notes": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
        }


#------------------- Campaign forms -------------------
class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = ["name", "description", "status", "start_date", "end_date", "target_list", "offer"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "status": forms.Select(attrs={"class": "form-select"}),
            "start_date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "end_date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "target_list": forms.TextInput(attrs={"class": "form-control", "placeholder": "Target list name"}),
            "offer": forms.Select(attrs={"class": "form-select"}),
        }        