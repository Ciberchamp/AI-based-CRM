from django import forms
from .models import Plan, Initiative, Tactic


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
